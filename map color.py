class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph  # Adjacency list representation of the graph
        self.colors = colors  # List of available colors
        self.color_assignment = {}  # Dictionary to store color assignments

    def is_safe(self, node, color):
        # Check if the color assignment is safe for the given node
        for neighbor in self.graph[node]:
            if neighbor in self.color_assignment and self.color_assignment[neighbor] == color:
                return False
        return True

    def backtrack(self, node):
        # If all nodes are assigned a color
        if node == len(self.graph):
            return True

        # Iterate over available colors
        for color in self.colors:
            if self.is_safe(node, color):
                self.color_assignment[node] = color  # Assign color

                # Recur to assign colors to the next node
                if self.backtrack(node + 1):
                    return True

                # If no color assignment was successful, remove the color (backtrack)
                del self.color_assignment[node]

        return False  # Trigger backtracking

    def solve(self):
        if self.backtrack(0):
            return self.color_assignment
        else:
            return None

if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }

    # Define the available colors
    colors = ['Red', 'Green', 'Blue']

    map_coloring = MapColoring(graph, colors)
    result = map_coloring.solve()

    if result:
        print("Color assignment:", result)
    else:
        print("No solution exists.")
