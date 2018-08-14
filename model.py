def step(world, goal_state, state, action):
    # input   (agent_state, box_states) action       box_states if tuple
    # output  (next_agent_state, next_box_state) reward
    # inout and output are tuple because tuple is hashable ,list is not hashable
    agent_state, box_states = state
    box_states = tuple(box_states)
    world_copy = world.copy()
    world_copy[agent_state[0], agent_state[1]] = 4
    for bs in box_states:
        world_copy[bs[0], bs[1]] = 3
    reward = 0
    if action == 0:  # up
        # meet wall, dont move
        next_agent_state = (agent_state[0] - 1, agent_state[1])
        if world_copy[next_agent_state[0], next_agent_state[1]] == 1:
            next_state = (agent_state, frozenset(box_states))
        # meet blank state or goal, agent move, box dont move
        elif world_copy[next_agent_state[0], next_agent_state[1]] == 0 or\
                world_copy[next_agent_state[0], next_agent_state[1]] == 2:
            next_state = (next_agent_state, frozenset(box_states))
        # meet box
        else:
            for i, box_state in enumerate(box_states):
                next_box_state = (box_state[0] - 1, box_state[1])
                if (next_agent_state[0], next_agent_state[1]) == box_state:
                    if world_copy[next_box_state[0], next_box_state[1]] == 1 or 3:  # box meet wall or box, dont move
                        next_state = (agent_state, frozenset(box_states))
                    if world_copy[next_box_state[0], next_box_state[1]] == 0 or\
                            world_copy[next_box_state[0], next_box_state[1]] == 2:  # box meet blank state or goal, move
                        box_states = list(box_states)
                        box_states[i] = next_box_state
                        next_state = (next_agent_state, frozenset(tuple(box_states)))

    elif action == 1:  # down
        # meet wall, dont move
        next_agent_state = (agent_state[0] + 1, agent_state[1])
        if world_copy[next_agent_state[0], next_agent_state[1]] == 1:
            next_state = (agent_state, frozenset(box_states))
        # meet blank state or goal, agent move, box dont move
        elif world_copy[next_agent_state[0], next_agent_state[1]] == 0 or world_copy[
            next_agent_state[0], next_agent_state[1]] == 2:
            next_state = (next_agent_state, frozenset(box_states))
        # meet box
        else:
            for i, box_state in enumerate(box_states):
                next_box_state = (box_state[0] + 1, box_state[1])
                if (next_agent_state[0], next_agent_state[1]) == box_state:
                    if world_copy[next_box_state[0], next_box_state[1]] == 1 or 3:  # box meet wall or box, dont move
                        next_state = (agent_state, frozenset(box_states))
                    if world_copy[next_box_state[0], next_box_state[1]] == 0 or\
                            world_copy[next_box_state[0], next_box_state[1]] == 2:  # box meet blank state or goal, move
                        box_states = list(box_states)
                        box_states[i] = next_box_state
                        next_state = (next_agent_state, frozenset(tuple(box_states)))
    elif action == 2:  # right
        # meet wall, dont move
        next_agent_state = (agent_state[0], agent_state[1] + 1)
        if world_copy[next_agent_state[0], next_agent_state[1]] == 1:
            next_state = (agent_state, frozenset(box_states))
        # meet blank state or goal, agent move, box dont move
        elif world_copy[next_agent_state[0], next_agent_state[1]] == 0 or \
                world_copy[next_agent_state[0], next_agent_state[1]] == 2:
            next_state = (next_agent_state, frozenset(box_states))
        # meet box
        else:
            for i, box_state in enumerate(box_states):
                next_box_state = (box_state[0], box_state[1] + 1)
                if (next_agent_state[0], next_agent_state[1]) == box_state:
                    if world_copy[next_box_state[0], next_box_state[1]] == 1 or 3:  # box meet wall or box, dont move
                        next_state = (agent_state, frozenset(box_states))
                    if world_copy[next_box_state[0], next_box_state[1]] == 0 or\
                            world_copy[next_box_state[0], next_box_state[1]] == 2:  # box meet blank state or goal, move
                        box_states = list(box_states)
                        box_states[i] = next_box_state
                        next_state = (next_agent_state, frozenset(tuple(box_states)))
    elif action == 3:  # left
        # meet wall, dont move
        next_agent_state = (agent_state[0], agent_state[1] - 1)
        if world_copy[next_agent_state[0], next_agent_state[1]] == 1:
            next_state = (agent_state, frozenset(box_states))
        # meet blank state or goal, agent move, box dont move
        elif world_copy[next_agent_state[0], next_agent_state[1]] == 0 or\
                world_copy[next_agent_state[0], next_agent_state[1]] == 2:
            next_state = (next_agent_state, frozenset(box_states))
        # meet box
        else:
            for i, box_state in enumerate(box_states):
                next_box_state = (box_state[0], box_state[1] - 1)
                if (next_agent_state[0], next_agent_state[1]) == box_state:
                    if world_copy[next_box_state[0], next_box_state[1]] == 1 or 3:  # box meet wall or box, dont move
                        next_state = (agent_state, frozenset(box_states))
                    if world_copy[next_box_state[0], next_box_state[1]] == 0 or\
                            world_copy[next_box_state[0], next_box_state[1]] == 2:  # box meet blank state or goal, move
                        box_states = list(box_states)
                        box_states[i] = next_box_state
                        next_state = (next_agent_state, frozenset(tuple(box_states)))

    if set(next_state[1]) == goal_state:
        reward = 1
    return next_state, reward
