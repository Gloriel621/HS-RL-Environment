from data import Hand, Buyers

import numpy as np


class State:
    def __init__(self):
        self.hand = Hand
        self.buyers = Buyers
        self.goods = 100

        self.state_to_numpy()

    def state_to_numpy(self):  # change to model input form
        np_hand = self.hand_to_numpy()
        np_buyers = self.buyers_to_numpy()
        np_goods = np.array([self.goods])
        state = np.concatenate([np_hand, np_buyers, np_goods])

        return state

    def hand_to_numpy(self):
        np_hand = np.fromiter(self.hand.values(), dtype=int)

        return np_hand

    def buyers_to_numpy(self):
        tmp = []
        for buyer in self.buyers:
            tmp.append(np.fromiter(buyer.values(), dtype=int))

        np_buyers = []
        for np_buyer in tmp:
            np_buyers = np.concatenate([np_buyers, np_buyer])

        return np_buyers
