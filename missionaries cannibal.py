from collections import deque
initial_state = (3, 3, 1)  
goal_state = (0, 0, 0)     
def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if (m_left >= 0 and m_right >= 0 and
        c_left >= 0 and c_right >= 0 and
        (m_left == 0 or m_left >= c_left) and
        (m_right == 0 or m_right >= c_right)):
        return True
    return False
def successors(state):
    m, c, boat = state
    possibilities = []
    if boat == 1:  
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]          
            new_state = (m - move[0], c - move[1], 0)  
            if is_valid(new_state):
                possibilities.append(new_state)
    else:  
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in moves:
            new_state = (m + move[0], c + move[1], 1)  
            if is_valid(new_state):
                possibilities.append(new_state)
    return possibilities
def bfs():
    queue = deque([(initial_state, [])])  
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        if current_state in visited:
            continue
        visited.add(current_state)

        for successor in successors(current_state):
            if successor not in visited:
                queue.append((successor, path + [current_state]))

    return None  
def print_solution(solution):
    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")
solution = bfs()
print_solution(solution)
