from environment import Environment


goods_action_list = [(0, 5), (6, 1), (0, 1), (16, 3), (16, 3)]

env = Environment()
env.reset()
for goods, action in goods_action_list:

    b = env.return_available_hand()
    print(b)
    print(env.return_available_action(goods), action)

    state, reward, done = env.step(goods, action)

    for goods in env.state.hand:
        if env.state.hand[goods] != 0:
            print(f"{goods}: {env.state.hand[goods]}")

    print(f"num_done : {env.num_solved}, step : {env.num_steps}\n")
