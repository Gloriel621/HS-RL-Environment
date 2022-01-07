from typing import OrderedDict
from state import State
from data import Sellers, Gold_Amount

import copy
import numpy as np
from collections import OrderedDict


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
    def Sell(self, goods: int, action: int):

        goods_list = Sellers[action]
        goods_str = list(self.state.hand.items())[goods][0]
        # goods = 현재 손패 중 내가 교환하고자 하는 것

        for exchange_list in goods_list:
            if goods_str == exchange_list[0]:
                amount = exchange_list[2]
                target = exchange_list[1]
                
                num_second = self.state.hand[goods_str] // amount
                self.state.hand[target] += num_second
                self.state.hand[goods_str] -= num_second * amount

    # actions 7 ~ 13
    def Buy(self, goods: int, action: int):

        buyer = self.state.buyers[action]
        gold = self.gold_amount[action]
        goods_str = list(self.state.hand.items())[goods][0]
        goods_index = list(OrderedDict(buyer).keys()).index(goods_str)

        self.state.hand["gold"] += gold[goods_index]
        self.state.hand[goods_str] -= buyer[goods_str]
        self.state.buyers[action][goods_str] = 0
        self.reward += 10
        self.num_solved += 1

    def return_available_hand(self):
        # return indices of available actions
        hand = self.state.hand_to_numpy()

        return np.where(hand > 0)[0]

    def return_available_action(self, goods_int):
        # 손패에 있는 교환하기로 한 물건에 대하여 갈 수 있는 action의 목록을 뽑아준다.
        # input goods는 int 형태

        available_action_list = []

        for action in range(7): # sellers
            goods_list = Sellers[action]

            for goods in goods_list:
                first = goods[0]
                amount = goods[2]

                if self.state.hand[first] >= amount:
                    available_action_list.append(action)
                    break

        goods_str = list(self.state.hand.items())[goods_int][0]

        for action in range(7): # buyers
            buyer = self.state.buyers[action]
            buyer_goods_list = list(buyer.keys())

            if (goods_str in buyer_goods_list) and buyer[goods_str] > 0 \
                and self.state.hand[goods_str] >= buyer[goods_str]:
                available_action_list.append(action + 7)

        return available_action_list


    def step(self, goods: int, action: int):

        prev_state = copy.deepcopy(self.state)

        if action >= 7:
            self.Buy(goods, action - 7)

        else:
            self.Sell(goods, action)

        #
        if (prev_state.hand == self.state.hand
                and prev_state.buyers == self.state.buyers):
            self.infeasible[action] = 1

        else:
            self.infeasible = np.zeros(self.num_actions)
            self.num_steps += 1
        # 여기 지워야 함

        if np.all(self.infeasible) or self.num_solved >= 35 or self.num_steps >= 250:
            self.done = True

        return self.state, self.reward, self.done

    def render(self):

        return
