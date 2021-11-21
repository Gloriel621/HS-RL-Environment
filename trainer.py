import copy

import structlog
import numpy as np
import torch
import torch.nn.functional as F
from torch.distributions import Categorical

from model import PPO
from environment import Environment

PRINT_INTERVAL = 10
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
                    prob = F.normalize(prob, dim=1, p=1.0)
                    categorical_distribution = Categorical(prob)

                    action = categorical_distribution.sample().item()
                    new_state, reward, done = self.env.step(action)
                    print(action, reward)
                    new_state = new_state.state_to_numpy()
                    self.model.put_data(
                        (
                            copy.deepcopy(state),
                            action,
                            float(reward / 64),
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
        torch.save(self.employee_model.state_dict(), f"hr_ppo_demo_{episode}.pt")

    def _init_hyperparameters(self):
        self.max_episodes = 5000
        self.mini_batch_size = 10
