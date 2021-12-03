import copy

import structlog
import numpy as np
import torch
import torch.nn.functional as F
from torch.distributions import Categorical

from model import PPO
from environment import Environment

PRINT_INTERVAL = 50
logger = structlog.get_logger(__name__)

action_list = [5, 1, 3, 0, 10, 5, 1, 3, 9, 5, 3, 2, 8, 11, 1, 6, 13, 1, 3, 12, 6, 8, 1, 6, 1, 4, 11,
               4, 3, 2, 1, 13, 3, 11, 3, 5, 5, 1, 10, 2, 5, 7, 2, 5, 8, 1, 3, 13, 1, 3, 6, 10, 0, 1,
               12, 5, 0, 4, 7, 0, 1, 3, 11, 5, 3, 2, 9, 0, 1, 3, 5, 12, 5, 3, 2, 0, 13, 6, 3, 8, 0, 1,
               4, 7, 5, 6, 11, 5, 0, 4, 9, 4, 7, 1, 6, 1, 10, 3, 5, 8, 0, 1, 3, 12, 3, 10, 5, 3, 2, 0,
               9, 5, 12, 2, 7, 2, 4, 9, 0, 13]


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
                    prob = prob * torch.from_numpy(1 - self.env.infeasible).float()
                    prob = F.normalize(prob, dim=1, p=1.0)
                    categorical_distribution = Categorical(prob)

                    action = categorical_distribution.sample().item()
                    new_state, reward, done = self.env.step(action)
                    new_state = new_state.state_to_numpy()
                    # print(action, reward)
                    # for goods in self.env.state.hand:
                    #     if self.env.state.hand[goods] != 0:
                    #         print(f"{goods}: {self.env.state.hand[goods]}")
                    self.model.put_data(
                        (
                            copy.deepcopy(state),
                            action,
                            float(reward / 128),
                            copy.deepcopy(new_state),
                            prob[0][action].item(),
                            done,
                        )
                    )
                    state = copy.deepcopy(new_state)
                    if done:
                        rewards.append(reward)
                        break
                self.model.train_net()
            # except Exception as e:
            #     logger.info(f"episode : {episode}, reward : {reward}")
            #     logger.error(e)
            #     self.model = PPO()
            #     episode = 0
            # else:
            episode += 1

            if episode % PRINT_INTERVAL == 0 and episode != 0:
                print("Episode :{}, avg reward : {:.2f}".format(episode, np.mean(rewards)))
                rewards = []
        torch.save(self.model.state_dict(), f"hr_ppo_demo_{episode}.pt")

    def _init_hyperparameters(self):
        self.max_episodes = 5000
        self.mini_batch_size = 25
