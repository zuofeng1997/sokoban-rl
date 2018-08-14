from sokoban.util import load_policy, pull_png
from sokoban.model import step
from sokoban.util import pic_to_matrix, swipe_screen


num_box = 0
gamma = 0.99
actions = [0, 1, 2, 3]  # up down right left
pull_png()
policy = load_policy("policys/policy10")
world, game_state, goal_state = pic_to_matrix("screen.png")
moves = []
while True:
    a = policy[game_state]
    if a == 0:
        moves.append(a)
    elif a == 1:
        moves.append(a)
    elif a == 2:
        moves.append(a)
    else:
        moves.append(a)

    game_state, reward = step(world, goal_state, game_state, a)
    if reward == 1:
        break
print("start move")
for move in moves:
    swipe_screen(move)

print("Congratulations! You win!")
print("Game over!")


