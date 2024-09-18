import heapq

class Node:
    def __init__(self, position, g=0, h=0):
        self.position = position  
        self.g = g  
        self.h = h
        self.f = g + h
        self.parent = None  

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    open_list = []
    closed_list = set()
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  
        
        closed_list.add(current_node.position)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for new_position in neighbors:
            neighbor_position = (current_node.position[0] + new_position[0],
                                 current_node.position[1] + new_position[1])
            if (0 <= neighbor_position[0] < len(grid) and
                0 <= neighbor_position[1] < len(grid[0]) and
                grid[neighbor_position[0]][neighbor_position[1]] == 0):
                
                if neighbor_position in closed_list:
                    continue  

                g_cost = current_node.g + 1
                h_cost = heuristic(neighbor_position, goal)
                neighbor_node = Node(neighbor_position, g_cost, h_cost)
                neighbor_node.parent = current_node

                
                if neighbor_node in open_list:
                    continue
                
                heapq.heappush(open_list, neighbor_node)

    return None 

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    start = (0, 0)  
    goal = (4, 4)   

    path = a_star(start, goal, grid)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
