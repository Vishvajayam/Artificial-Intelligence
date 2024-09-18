from collections import deque

def water_jug_problem(jug1, jug2, target):
    # Create a queue for BFS
    queue = deque()
    # Set to keep track of visited states
    visited = set()

    # Initial state (0, 0) - both jugs are empty
    initial_state = (0, 0)
    queue.append((initial_state, []))  # Append the initial state with an empty path

    while queue:
        (current_jug1, current_jug2), path = queue.popleft()

        # Check if we reached the target
        if current_jug1 == target or current_jug2 == target:
            path.append((current_jug1, current_jug2))
            return path

        # Mark this state as visited
        if (current_jug1, current_jug2) in visited:
            continue
        visited.add((current_jug1, current_jug2))

        # Possible next states
        next_states = [
            (jug1, current_jug2),  # Fill jug1
            (current_jug1, jug2),  # Fill jug2
            (0, current_jug2),     # Empty jug1
            (current_jug1, 0),     # Empty jug2
            (min(current_jug1 + current_jug2, jug1), current_jug2 - (jug1 - current_jug1) if current_jug2 >= (jug1 - current_jug1) else 0),  # Pour jug2 into jug1
            (current_jug1 - (jug2 - current_jug2) if current_jug1 >= (jug2 - current_jug2) else 0, min(current_jug1 + current_jug2, jug2))  # Pour jug1 into jug2
        ]

        # Enqueue all possible next states
        for state in next_states:
            queue.append((state, path + [(current_jug1, current_jug2)]))

    return None  # If no solution found

if __name__ == "__main__":
    # Example capacities of the jugs and the target amount
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

    if solution:
        print("Steps to achieve target:")
        for step in solution:
            print(f"Jug1: {step[0]}, Jug2: {step[1]}")
    else:
        print("No solution found.")
