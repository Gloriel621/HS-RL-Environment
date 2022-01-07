from environment import Environment

import numpy as np

goods_action_list = [(0, 5), (0, 1), (6, 3), (2, 0), (12, 10), (0, 5), (0, 1), (6, 3), (2, 9)]

env = Environment()
env.reset()
for goods, action in goods_action_list:

    b = env.return_available_hand()
    print(env.return_available_action(goods), action)

    state, reward, done = env.step(goods, action)