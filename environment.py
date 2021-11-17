from state import State
from data import Sellers, Buyers, Gold_Amount
import copy


class Environment:
    def __init__(self):
        self.num_actions = 14
        self.init_state = State()
        self.init_sellers = Sellers
        self.init_buyers = Buyers
        self.gold_amount = Gold_Amount

        self.state_class = copy.deepcopy(self.init_state)
        self.sellers = copy.deepcopy(self.init_sellers)
        self.buyers = copy.deepcopy(self.init_buyers)

    def reset(self):
        self.done = False
        self.num_steps = 0
        self.reward = 0

        self.state_class = copy.deepcopy(self.init_state)
        self.sellers = copy.deepcopy(self.init_sellers)
        self.buyers = copy.deepcopy(self.init_buyers)

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

    # action 7 ~ 13
    def Buy(self, action: int):

        action = action - 7
        buyer = self.state.buyers[action]
        gold = self.gold_amount[action]

        count = 0
        for goods in buyer:
            if buyer[goods] > 0 and self.state.hand[goods] >= buyer[goods]:
                self.state.hand["gold"] += gold[count]
                self.state.hand[goods] -= buyer[goods]
                self.state.buyers[action][goods] = 0
            count += 1

    def Trade(self, action: int, state: State):

        if action >= 7:
            state = self.Buy(action, state)

        else:
            state = self.Sell(action, state)

        return state

    def step(self, action: int):

        # Buyers 들 검사해서 다 샀으면 보상 추가
        self.reward += 0

        # done = True 만드는 조건? 일단 모든 buyer들이 다 샀으면 끝내는 거로 하고 싶긴 함
        if self.num_steps == 1000:
            self.done = True

        return self.state_class, self.reward, self.done

    def cal_reward(self):

        return

    def render(self):

        return
