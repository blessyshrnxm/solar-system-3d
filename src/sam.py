def monkey_banana_problem():
    # Initial state: (Monkey_Location, Chair_Position, Monkey_Position, Monkey_Status)
    initial_state = ('Far-Chair', 'Chair-Not-Under-Banana', 'Off-Chair', 'Empty')
    print(f"\nInitial state: {initial_state}")

    # Goal state
    goal_state = ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', 'Holding')

    # Actions and their effects
    actions = {
        "Move to Chair": lambda state: ('Near-Chair', state[1], state[2], state[3])
        if state[0] != 'Near-Chair' else None,

        "Push Chair under Banana": lambda state: ('Near-Chair', 'Chair-Under-Banana', state[2], state[3])
        if state[0] == 'Near-Chair' and state[1] != 'Chair-Under-Banana' else None,

        "Climb Chair": lambda state: ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', state[3])
        if state[0] == 'Near-Chair' and state[1] == 'Chair-Under-Banana' and state[2] != 'On-Chair' else None,

        "Grasp Banana": lambda state: ('Near-Chair', 'Chair-Under-Banana', 'On-Chair', 'Holding')
        if state[0] == 'Near-Chair' and state[1] == 'Chair-Under-Banana' and state[2] == 'On-Chair' and state[3] != 'Holding' else None
    }

    # BFS Algorithm to find sequence of actions
    from collections import deque
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            print("\nSequence of actions to reach the banana:")
            for step, action in enumerate(path, 1):
                print(f"{step}. {action}")
            print(f"\nFinal State: {current_state}")
            return

        if current_state not in visited:
            visited.add(current_state)
            for action_name, action_func in actions.items():
                next_state = action_func(current_state)
                if next_state and next_state not in visited:
                    queue.append((next_state, path + [action_name]))

    print("No solution found.")

# Run the Monkey Banana Problem
monkey_banana_problem()
