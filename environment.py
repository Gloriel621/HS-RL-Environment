import numpy as np
from data import Hand, Sellers, Buyers, Buyers_gold


class State:
    def __init__(self):
        self.hand = Hand
        self.buyers = Buyers

        self.state_to_numpy()

    def state_to_numpy(self):  # change to model input form
        np_hand = np.fromiter(self.hand.values(), dtype=int)

        np_buyers = []
        for buyer in self.buyers:
            np_buyers.append(np.fromiter(buyer.values(), dtype=int))

        self.state = np_hand
        for np_buyer in np_buyers:
            self.state = np.concatenate([self.state, np_buyer], dtype=int)


# action 0 ~ 6
def Sell(action: int, state: State):  # 나중에 클래스 안에 넣고 state 사용하는 거로 바꾸기.

    goods_list = Sellers[action]

    for goods in goods_list:
        first = goods[0]
        second = goods[1]
        amount = goods[2]

        if state.hand[first] >= amount:
            num_second = state.hand[first] // amount
            state.hand[second] += num_second
            state.hand[first] -= num_second * amount
            return state

    return state


# action 7 ~ 13
def Buy(action: int, state: State):

    action = action - 7
    buyer = state.buyers[action]
    gold = Buyers_gold[action]

    count = 0
    for goods in buyer:
        if buyer[goods] > 0 and state.hand[goods] >= buyer[goods]:
            # 사람이 필요로 하는 물건의 개수가 0보다 크고
            # 현재 손패에 들고 있는 물건의 개수가 필요로 하는 물건 개수 이상일 때
            state.hand["gold"] += gold[count]
            state.hand[goods] -= buyer[goods]
            state.buyers[action][goods] = 0
            return state
        count += 1

    return state


def Trade(action: int, state: State):

    if action >= 7:
        state = Buy(action, state)

    else:
        state = Sell(action, state)

    return state
