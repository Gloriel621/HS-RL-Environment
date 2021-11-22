from state import State
from data import Sellers, Gold_Amount

import copy


class Environment:
    def __init__(self):
        self.num_actions = 14
        self.init_state = State()
        self.init_sellers = Sellers
        self.gold_amount = Gold_Amount

        self.state = copy.deepcopy(self.init_state)
        self.sellers = copy.deepcopy(self.init_sellers)

    def reset(self):
        self.done = False
        self.num_steps = 0
        self.reward = 0

        self.state = copy.deepcopy(self.init_state)
        self.sellers = copy.deepcopy(self.init_sellers)

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

        num_done = 0
        action = action - 7
        buyer = self.state.buyers[action]
        gold = self.gold_amount[action]

        count = 0
        for goods in buyer:
            if buyer[goods] > 0 and self.state.hand[goods] >= buyer[goods]:
                self.state.hand["gold"] += gold[count]
                self.state.hand[goods] -= buyer[goods]
                self.state.buyers[action][goods] = 0
                num_done += 1
                break
            count += 1

        return num_done

    def step(self, action: int):

        if action >= 7:
            buy = self.Buy(action)
            if buy == 0:
                self.reward -= 0.1
            else:
                self.reward += 1

        else:
            self.Sell(action)

        self.num_steps += 1

        if self.reward == 35 or self.num_steps >= 500:
            self.done = True

        return self.state, self.reward, self.done

    def render(self):

        return
