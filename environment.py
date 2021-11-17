import numpy as np
from data import Merchants, Buyers


class State:
    def __init__(self):
        self.hand = {
            "gold": 10,
            "hand_axe": 0,  # 손도끼
            "linen_bandage": 0,  # 리넨 붕대
            "stormwind_cheddar": 0,  # 스톰윈드 체더 치즈
            "cute_doll": 0,  # 귀여운 인형
            "shadowy_gem": 0,  # 그림자 보석
            "elixir_of_vigor": 0,  # 재활의 물약
            "potions_of_night": 0,  # 밤의 물약
            "gnomish_shield": 0,  # 노움 방패
            "loyal_pet_whistle": 0,  # 충직의 애완동물 호루라기
            "very_nice_hat": 0,  # 아주 멋진 모자
            "angry_cristal": 0,  # 화난 수정
            "jade_locket": 0,  # 비취 은감 목걸이
            "goblin_fishing_pole": 0,  # 고블린 낚시 도구
            "captivating_pipe": 0,  # 매료의 피리
            "healing_potion": 0,  # 치유 물약
            "iron_dagger": 0,  # , 강철 단검
            "arcane_scroll": 0,  # 비전 두루마리
            "golden_goblet": 0,  # 황금 술잔
            "sapphire_wand": 0,  # 사파이어 마법봉
            "everburning_candle": 0,  # 영원히 타오르는 양초
            "ruby_crown": 0,  # 루비 왕관
            "alliance_mace": 0,  # 얼라이언스 철퇴
            "draught_of_angels": 0,  # 천사의 비약
            "gilneas_dagger": 0,  # 길니아스 단검
            "tiger_amulet": 0,  # 호랑이 부적
            "sphere_of_wisdom": 0,  # 지혜의 구슬
        }
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

def Sell(action: int, hand: State.hand):  # 나중에 클래스 안에 넣고 state사용하는 거로 바꾸기.

    goods_list = Merchants[action]

    for goods in goods_list:
        first = goods[0]
        second = goods[1]
        amount = goods[2]

        if hand[first] >= amount:
            num_second = hand[first] // amount
            hand[second] = num_second
            hand[first] = hand[first] - num_second * amount
            return hand

    return hand

def Buy(action: int, state: State):
    pass
