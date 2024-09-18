import itertools

class TravelingSalesman:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def calculate_route_cost(self, route):
        cost = 0
        for i in range(len(route)):
            cost += self.distance_matrix[route[i]][route[(i + 1) % len(route)]]
        return cost

    def solve(self):
        cities = list(range(self.num_cities))
        min_cost = float('inf')
        best_route = None

        for route in itertools.permutations(cities):
            cost = self.calculate_route_cost(route)
            if cost < min_cost:
                min_cost = cost
                best_route = route

        return best_route, min_cost

if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp = TravelingSalesman(distance_matrix)
    best_route, min_cost = tsp.solve()

    print("Best route:", best_route)
    print("Minimum cost:", min_cost)
