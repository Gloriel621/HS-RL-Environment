# https://www.hearthpwn.com/news/8230-mysteries-of-the-phoenix-druid-and-hunter-puzzles
from environment import Environment
from model import PPO
import copy
import numpy as np
import torch
import torch.nn.functional as F
from torch.distributions import Categorical

# Baloon_Merchant 0
# Armor_Vender 1
# Barrens_Blacksmith 2
# Darkshire_Alchemist 3
# Shady_dealer 4
# Master_Swordsmith 5
# Drakkari_Enchanter 6

# dalaran_mage 7
# bloodsail_corsair 8
# violet_apprentice 9
# silver_hand_knight 10
# darnassus_aspirant 11
# windspeaker 12
# defender_of_argus 13

goods_action_list = [(0, 5), (0, 1), (6, 3), (2, 0), (12, 10), (0, 5), (0, 1), (6, 3), (2, 9), (0, 5)]

action_list = [5, 1, 3, 0, 10, 5, 1, 3, 9, 5, 3, 2, 8, 11, 1, 6, 13, 1, 3, 12, 6, 8, 1, 6, 1, 4, 11,
               4, 3, 2, 1, 13, 3, 11, 3, 5, 5, 1, 10, 2, 5, 7, 2, 5, 8, 1, 3, 13, 1, 3, 6, 10, 0, 1,
               12, 5, 0, 4, 7, 0, 1, 3, 11, 5, 3, 2, 9, 0, 1, 3, 5, 12, 5, 3, 2, 0, 13, 6, 3, 8, 0, 1,
               4, 7, 5, 6, 11, 5, 0, 4, 9, 4, 7, 1, 6, 1, 10, 3, 5, 8, 0, 1, 3, 12, 3, 10, 5, 3, 2, 0,
               9, 5, 12, 2, 7, 2, 4, 9, 0, 13]

env = Environment()
env.reset()
model = PPO()

state = copy.deepcopy(env.state)
state = state.state_to_numpy()
done = env.done

for i in range(10):

    prob = model.pi(state)
    available_hands = env.return_available_hand()
    # select hand

    if not np.any(available_hands):
        env.done = True
        # nothing in hands to select
        print("nothing in hands to select")
        break

    available = np.concatenate([available_hands, np.zeros(14)])
    prob = prob * torch.from_numpy(available).float()
    prob = F.normalize(prob, dim=1, p=1.0)
    categorical_distribution = Categorical(prob)
    hand = categorical_distribution.sample().item()
    prob2 = model.pi(state, np.array([hand]))
    available_actions = env.return_available_action(hand)
    # select action

    # error handling
    if not np.any(available_actions):
        env.done = True
        # no actions to select
        print("no actions to select")

    available = np.concatenate([np.zeros(27), available_actions])
    prob2 = prob2 * torch.from_numpy(available).float()
    prob2 = F.normalize(prob2, dim=1, p=1.0)
    categorical_distribution = Categorical(prob2)
    action = categorical_distribution.sample().item()
    action = action - 27

    # hand, action = goods_action_list[i]

    print(f"selected item in hand : {list(env.state.hand.items())[hand][0]}({hand}) , action : {action}")

    new_state, reward, done = env.step(hand, action)
    new_state = new_state.state_to_numpy()
    state = copy.deepcopy(new_state)

    for goods in env.state.hand:
        if env.state.hand[goods] != 0:
            print(f"{goods}: {env.state.hand[goods]}")

    print(f"num_done : {env.num_solved}, step : {env.num_steps}\n")

# for goods, action in goods_action_list:
#     state, reward, done = env.step(goods, action)

#     for goods in env.state.hand:
#         if env.state.hand[goods] != 0:
#             print(f"{goods}: {env.state.hand[goods]}")

#     print(f"num_done : {env.num_solved}, step : {env.num_steps}\n")
