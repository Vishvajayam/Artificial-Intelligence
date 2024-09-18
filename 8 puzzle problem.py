import heapq
def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            x1, y1 = divmod(i, 3)          
            x2, y2 = divmod(goal.index(state[i]), 3)  
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def generate_moves(state):
    neighbors = []
    blank_index = state.index(0)  
    row, col = divmod(blank_index, 3)
    moves = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    
    for r, c in moves:
        if 0 <= r < 3 and 0 <= c < 3:  
            new_state = state[:]
            new_blank_index = r * 3 + c
            new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
            neighbors.append(new_state)
    
    return neighbors
def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start, 0, []))  
    visited = set()
    
    while open_list:
        f, current_state, g, path = heapq.heappop(open_list)
        if current_state == goal:
            return path + [current_state]
        if tuple(current_state) in visited:
            continue
        visited.add(tuple(current_state))
        for neighbor in generate_moves(current_state):
            if tuple(neighbor) not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (new_f, neighbor, new_g, path + [current_state]))

    return None 
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
start_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]   
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
solution = astar(start_state, goal_state)
if solution:
    print("Solution found in {} moves!".format(len(solution) - 1))
    for step in solution:
        print_puzzle(step)
else:
    print("No solution found.")
