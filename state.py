from data import Hand, Buyers

import numpy as np


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
