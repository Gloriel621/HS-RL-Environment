from state import State
from data import Sellers, Gold_Amount

import copy
import numpy as np


class Environment:
    def __init__(self):
        self.num_actions = 14
        self.init_state = State()
        self.init_sellers = Sellers
        self.gold_amount = Gold_Amount

    def reset(self):
        self.done = False
        self.num_steps = 0
        self.reward = 0
        self.num_solved = 0

        self.state = copy.deepcopy(self.init_state)
        self.infeasible = np.zeros(self.num_actions)

    # actions 0 ~ 6
    def Sell(self, action: int):

        goods_list = Sellers[action]

        for goods in goods_list:
            first = goods[0]
            second = goods[1]
            amount = goods[2]

            if self.state.hand[first] >= amount:
                num_second = self.state.hand[first] // amount
                self.state.hand[second] += num_second
                self.state.hand[first] -= num_second * amount
                break

    # actions 7 ~ 13
    def Buy(self, action: int):

        buyer = self.state.buyers[action]
        gold = self.gold_amount[action]

        count = 0
        for goods in buyer:
            if buyer[goods] > 0 and self.state.hand[goods] >= buyer[goods]:
                self.state.hand["gold"] += gold[count]
                self.state.hand[goods] -= buyer[goods]
                self.state.buyers[action][goods] = 0
                self.reward += 10
                self.num_solved += 1
                break
            count += 1

    def step(self, action: int):

        prev_state = copy.deepcopy(self.state)

        if action >= 7:
            self.Buy(action - 7)

        else:
            self.Sell(action)

        if (prev_state.hand == self.state.hand
                and prev_state.buyers == self.state.buyers):
            self.infeasible[action] = 1

        else:
            self.infeasible = np.zeros(self.num_actions)
            self.num_steps += 1

        if np.all(self.infeasible) or self.num_solved >= 35 or self.num_steps >= 250:
            self.done = True

        return self.state, self.reward, self.done

    def render(self):

        return
