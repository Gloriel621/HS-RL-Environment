import copy

import structlog
import numpy as np
import torch
import torch.nn.functional as F
from torch.distributions import Categorical

from model import PPO
from environment import Environment

PRINT_INTERVAL = 200
logger = structlog.get_logger(__name__)


class Trainer:
    def __init__(self):
        self._init_hyperparameters()
        self.env = Environment()
        self.env.reset()
        self.model = PPO()

    def train(self):
        rewards = []
        episode = 0
        while episode <= self.max_episodes:
            self.env.reset()
            state = copy.deepcopy(self.env.state)
            state = state.state_to_numpy()
            done = self.env.done

            # try:
            while not done:
                for t in range(self.mini_batch_size):
                    prob = self.model.pi(torch.from_numpy(state).float())
                    available_hands = self.env.return_available_hand()
                    available = np.concatenate([available_hands, np.zeros(14)])
                    prob = prob * torch.from_numpy(available).float()
                    prob = F.normalize(prob, dim=1, p=1.0)

                    categorical_distribution = Categorical(prob)
                    # select hand
                    hand = categorical_distribution.sample().item()
                    prev_state = copy.deepcopy(state)
                    self.env.state.goods = hand
                    state = self.env.state.state_to_numpy()
                    # print(prob)

                    self.model.put_data(
                        (
                            copy.deepcopy(prev_state),
                            hand,
                            float(self.env.reward / 128),
                            copy.deepcopy(state),
                            prob[0][hand].item(),
                            done,
                        )
                    )

                    prob2 = self.model.pi(torch.from_numpy(state).float())
                    available_actions = self.env.return_available_action(hand)
                    # select action

                    # error handling
                    if not np.any(available_actions):
                        self.env.done = True
                        done = True
                        break

                    available = np.concatenate([np.zeros(27), available_actions])
                    prob2 = prob2 * torch.from_numpy(available).float()
                    prob2 = F.normalize(prob2, dim=1, p=1.0)
                    categorical_distribution = Categorical(prob2)
                    action = categorical_distribution.sample().item()

                    new_state, reward, done = self.env.step(hand, action - 27)
                    new_state = new_state.state_to_numpy()

                    # for goods in self.env.state.hand:
                    #     if self.env.state.hand[goods] != 0:
                    #         print(f"{goods}: {self.env.state.hand[goods]}")

                    # print(f"num_done : {self.env.num_solved}, step : {self.env.num_steps}\n")

                    self.model.put_data(
                        (
                            copy.deepcopy(state),
                            action,
                            float(reward / 128),
                            copy.deepcopy(new_state),
                            prob2[0][action].item(),
                            done,
                        )
                    )
                    state = copy.deepcopy(new_state)
                self.model.train_net()

                if done:
                    rewards.append(reward)
                    break

            # except Exception as e:
            #     logger.info(f"episode : {episode}, reward : {reward}")
            #     logger.error(e)
            #     self.model = PPO()
            #     episode = 0
            # else:
            episode += 1

            if episode % PRINT_INTERVAL == 0 and episode != 0:
                print("Episode :{}, avg reward : {:.2f}, max reward : {:.2f}".format(
                    episode, np.mean(rewards), max(rewards)))
                rewards = []
        torch.save(self.model.state_dict(), f"hr_ppo_demo_{episode}.pt")

    def _init_hyperparameters(self):
        self.max_episodes = 50000
        self.mini_batch_size = 100
