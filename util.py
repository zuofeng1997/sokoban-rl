import pickle
import cv2
import numpy as np
import os


def save_policy(policy, name):
    fw = open(name, 'wb')
    pickle.dump(policy, fw)
    fw.close()


def load_policy(name):
    fr = open(name, 'rb')
    policy = pickle.load(fr)
    fr.close()
    return policy


def pull_png():   # get the picture of the game
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')


def swipe_screen(action):
    if action == 0:
        os.system("adb shell input swipe 250 600 250 300 100 ")
    if action == 1:
        os.system("adb shell input swipe 250 300 250 600 100")
    if action == 2:
        os.system("adb shell input swipe 250 300 500 300 100")
    if action == 3:
        os.system("adb shell input swipe 500 300 250 300 100")


def is_blank_inside(x, y, world):  # find the blank state inside the wall

    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    for i in range(x):
        if world[i, y] == 1:
            flag1 = True
    for i in range(x+1, world.shape[0]):
        if world[i, y] == 1:
            flag2 = True
    for j in range(y):
        if world[x, j] == 1:
            flag3 = True
    for j in range(y+1, world.shape[1]):
        if world[x, j] == 1:
            flag4 = True
    if flag1 and flag2 and flag3 and flag4:
        return True
    else:
        return False


def init_value_fn(world, num_box):  # initialize value function
    middle_blank = []
    value = dict()
    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            if world[i, j] == 0:
                if is_blank_inside(i, j, world):
                    middle_blank.append((i, j))
    print(middle_blank.__len__())
    box_states = []
    if num_box == 1:
        for agent in middle_blank:
            for box1 in middle_blank:
                if state_is_same([agent, box1]):
                    continue
                box_states.append(box1)
                value[(agent, frozenset(box_states))] = 0
                box_states = []
    elif num_box == 2:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    if state_is_same([agent, box1, box2]):
                        continue
                    box_states.append(box1)
                    box_states.append(box2)
                    value[(agent, frozenset(box_states))] = 0
                    box_states = []
    elif num_box == 3:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    for box3 in middle_blank:
                        if state_is_same([agent, box1, box2, box3]):
                            continue
                        box_states.append(box1)
                        box_states.append(box2)
                        box_states.append(box3)
                        value[(agent, frozenset(box_states))] = 0
                        box_states = []

    elif num_box == 4:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    for box3 in middle_blank:
                        for box4 in middle_blank:
                            if state_is_same([agent, box1, box2, box3, box4]):
                                continue
                            box_states.append(box1)
                            box_states.append(box2)
                            box_states.append(box3)
                            box_states.append(box4)
                            value[(agent, frozenset(box_states))] = 0
                            box_states = []
    elif num_box == 5:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    for box3 in middle_blank:
                        for box4 in middle_blank:
                            for box5 in middle_blank:
                                if state_is_same([agent, box1, box2, box3, box4, box5]):
                                    continue
                                box_states.append(box1)
                                box_states.append(box2)
                                box_states.append(box3)
                                box_states.append(box4)
                                box_states.append(box5)
                                value[(agent, frozenset(box_states))] = 0
                                box_states = []
    elif num_box == 6:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    for box3 in middle_blank:
                        for box4 in middle_blank:
                            for box5 in middle_blank:
                                for box6 in middle_blank:
                                    if state_is_same([agent, box1, box2, box3, box4, box5, box6]):
                                        continue
                                    box_states.append(box1)
                                    box_states.append(box2)
                                    box_states.append(box3)
                                    box_states.append(box4)
                                    box_states.append(box5)
                                    box_states.append(box6)
                                    value[(agent, frozenset(box_states))] = 0
                                    box_states = []

    elif num_box == 7:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    for box3 in middle_blank:
                        for box4 in middle_blank:
                            for box5 in middle_blank:
                                for box6 in middle_blank:
                                    for box7 in middle_blank:
                                        if state_is_same([agent, box1, box2, box3, box4, box5, box6, box7]):
                                            continue
                                        box_states.append(box1)
                                        box_states.append(box2)
                                        box_states.append(box3)
                                        box_states.append(box4)
                                        box_states.append(box5)
                                        box_states.append(box6)
                                        box_states.append(box7)
                                        value[(agent, frozenset(box_states))] = 0
                                        box_states = []
    elif num_box == 7:
        for agent in middle_blank:
            for box1 in middle_blank:
                for box2 in middle_blank:
                    for box3 in middle_blank:
                        for box4 in middle_blank:
                            for box5 in middle_blank:
                                for box6 in middle_blank:
                                    for box7 in middle_blank:
                                        for box8 in middle_blank:
                                            if state_is_same([agent, box1, box2, box3, box4, box5, box6, box7, box8]):
                                                continue
                                            box_states.append(box1)
                                            box_states.append(box2)
                                            box_states.append(box3)
                                            box_states.append(box4)
                                            box_states.append(box5)
                                            box_states.append(box6)
                                            box_states.append(box7)
                                            box_states.append(box8)
                                            value[(agent, frozenset(box_states))] = 0
                                            box_states = []

    return value


def state_is_same(states):
    if len(set(states)) == len(states):
        return False
    else:
        return True


def pic_to_matrix(pic, is_mix=False):
    # ugly way to transfer picture to matrix, if you want to play other games, you can just adjust this function.
    m = cv2.imread(pic)
    m = m[275:1740, :, :]
    block_size = 10

    m = cv2.resize(m, (120, 160))
    m = m[:, :, 1]
    box_state = set()
    goal_state = set()
    m_copy = np.zeros((16, 12))
    wall_and_agent = dict()
    box_and_goal = dict()
    blank_and_mix = dict()
    for i in range(16):
        for j in range(12):
            m_copy[i, j] = np.round(np.mean(m[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size])/10, 1)
            m_leftdown = m[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
            m_leftdown = np.sum(m_leftdown[:2, :])
            if m_copy[i, j] < 13:
                m_copy[i, j] = 1
                wall_and_agent[m_leftdown] = (i, j)
            elif m_copy[i, j] >= 17:
                blank_and_mix[m_copy[i, j]] = (i, j)
                m_copy[i, j] = 0
            else:
                m_copy[i, j] = 0
                box_and_goal[m_leftdown] = (i, j)

    if is_mix:
        mix_state = blank_and_mix[np.min(list(blank_and_mix.keys()))]
        goal_state.add(mix_state)
        box_state.add(mix_state)
    agent_state = wall_and_agent[np.max(list(wall_and_agent.keys()))]
    m_copy[agent_state[0], agent_state[1]] = 0
    k = list(box_and_goal.keys())
    k.sort()
    for ll in k[(len(k)//2):]:
        goal_state.add(box_and_goal[ll])
    for ll in k[:(len(k)//2)]:
        box_state.add(box_and_goal[ll])

    m_copy = np.concatenate((m_copy, np.ones((16, 1))), axis=1)
    return m_copy, (agent_state, frozenset(box_state)), goal_state


if __name__ == '__main__':

    world,a,b = pic_to_matrix("screen.png")
    print(world,a,b)

    # pull_png()

