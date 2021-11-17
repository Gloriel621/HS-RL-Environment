import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class PPO(nn.Module):
    def __init__(self):
        super(PPO, self).__init__()
        self.init_hyperparameters()

        self.data = []
        self.num_actions = 14

        self.fc1 = nn.Linear(self.num_actions, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc_pi = nn.Linear(256, self.num_actions)
        self.fc_v = nn.Linear(256, 1)
        self.optimizer = optim.Adam(self.parameters(), lr=self.learning_rate)

    def pi(self, x, softmax_dim=1):

        x = x.reshape(-1, self.num_actions)
        x = F.elu(self.fc1(x))
        x = F.elu(self.fc2(x))
        x = self.fc_pi(x)
        prob = F.softmax(x, dim=softmax_dim)
        return prob

    def v(self, x):
        x = x.reshape(-1, self.num_actions)
        x = F.elu(self.fc1(x))
        x = F.elu(self.fc2(x))
        v = self.fc_v(x)
        return v

    def put_data(self, transition):
        self.data.append(transition)

    def make_batch(self):
        (
            state_list,
            action_list,
            reward_list,
            state_prime_list,
            prob_action_list,
            done_list,
        ) = ([], [], [], [], [], [])

        for transition in self.data:
            state, action, reward, state_prime, prob_action, done = transition

            state_list.append(state)
            action_list.append([action])
            reward_list.append([reward])

            state_prime_list.append(state_prime)
            prob_action_list.append([prob_action])
            done_mask = 0 if done else 1
            done_list.append([done_mask])

        state, action, reward, state_prime, done_mask, prob_action = (
            torch.tensor(state_list, dtype=torch.float),
            torch.tensor(action_list),
            torch.tensor(reward_list),
            torch.tensor(state_prime_list, dtype=torch.float),
            torch.tensor(done_list, dtype=torch.float),
            torch.tensor(prob_action_list),
        )

        self.data = []
        return state, action, reward, state_prime, done_mask, prob_action

    def train_net(self):
        state, action, reward, state_prime, done_mask, prob_action = self.make_batch()

        for i in range(self.K_epoch):

            td_target = reward + self.gamma * self.v(state_prime) * done_mask
            delta = td_target - self.v(state)
            delta = delta.detach().numpy()

            advantage_list = []
            advantage = 0.0
            for delta_t in delta[::-1]:
                advantage = self.gamma * self.lmbda * self.v(state_prime) * done_mask
                advantage_list.append([advantage])
            advantage_list.reverse()
            advantage = torch.tensor(advantage_list, dtype=torch.float)

            pi = self.pi(state, softmax_dim=1)
            pi_action = pi.gather(1, action)
            ratio = torch.exp(torch.log(pi_action) - torch.log(prob_action))

            surr1 = ratio * advantage
            surr2 = torch.clamp(ratio, 1 - self.eps_clip, 1 + self.eps_clip) * advantage
            loss = -torch.min(surr1, surr2) + F.smooth_l1_loss(
                td_target.detach(), self.v(state)
            )

            self.optimizer.zero_grad()
            loss.mean().backward()
            self.optimizer.step()

    def init_hyperparameters(self):
        self.gamma = 0.98
        self.lmbda = 0.98
        self.K_epoch = 1
        self.eps_clip = 0.1
        self.learning_rate = 0.001
