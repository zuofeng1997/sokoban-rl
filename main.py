# 8 blank state beyond the wall
# 2 goal
# 0 blank state
# 1 wall
# 3 box
# 4 agent

import numpy as np
from sokoban.util import save_policy, init_value_fn, pull_png
from sokoban.model import step
from sokoban.util import pic_to_matrix

num_box = 0
gamma = 0.99
actions = [0, 1, 2, 3]  # up down right left
value = dict()
policy = dict()
pull_png()
world, game_state, goal_state = pic_to_matrix("screen.png")

num_box = len(game_state[1])
print(num_box)
value = init_value_fn(world, num_box)
print(value.keys().__len__())

# value iter
while True:
    delta = 0
    for state in value.keys():
        old_v = value[state]
        value_estimate = []
        for a in actions:
            next_state, reward = step(world, goal_state, state, a)

            value_estimate.append(reward+gamma*value[next_state])
        value[state] = np.max(value_estimate)
        delta = np.max([delta, np.abs(old_v-value[state])])
    print(delta)
    if delta < 1:
        break
print("find optimal value function")


# get optimal policy
for state in value.keys():
    value_estimate = []
    for a in actions:
        next_state, reward = step(world, goal_state, state, a)
        value_estimate.append(reward+gamma*value[next_state])
    a = np.argmax(value_estimate)
    policy[state] = a

save_policy(policy, "policys/policy11")  # policy name: policy + game level

