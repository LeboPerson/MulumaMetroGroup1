
from collections import deque

class Graph:
    def __init__(self):
        self.routes = {}   

    def add_city(self, city):
        if city not in self.routes:
            self.routes[city] = []

    def add_route(self, city1, city2, distance):
        self.add_city(city1)
        self.add_city(city2)
        self.routes[city1].append((city2, distance))
        self.routes[city2].append((city1, distance))  

g = Graph()


g.add_route("Johannesburg", "Pretoria", 300)
g.add_route("Johanesburg", "Durban", 50)
g.add_route("pretoria", "Polokwane", 200)
g.add_route("Cape Town", "Malawi", 2000)
  
#for city, neighbors in g.routes.items():
 #   print(f"{city} connected to: {neighbors}")



def find_shortest_route(graph, start, end): #Dijkstra algorythm
    distances = {city: float('inf') for city in graph.routes}
    previous = {city: None for city in graph.routes}
    visited = set()

    distances[start] = 0
    queue = deque()
    queue.append((start, 0))  

    while queue:
        current_city, current_distance = min(queue, key=lambda x: x[1])
        queue.remove((current_city, current_distance))

        if current_city in visited:
            continue
        visited.add(current_city)

        for neighbor, edge_cost in graph.routes[current_city]:
            new_distance = current_distance + edge_cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_city
                queue.append((neighbor, new_distance))

    # Path construction
    path = []
    city = end
    while city is not None:
        path.insert(0, city)  # Insert at the beginning to reverse the order
        city = previous[city]

    if distances[end] == float('inf'):
        return None, None  # No path found
    return path, distances[end]  # Return the path and total distance


"""
g = Graph()
g.add_route("Johannesburg", "Pretoria", 300)
g.add_route("Johannesburg", "Durban", 50)
g.add_route("Pretoria", "Polokwane", 200)
g.add_route("Cape Town", "Malawi", 2000)

start = "Johannesburg"
end = "Polokwane"
path, total = find_shortest_route(g, start, end)

if path:
    print(f"Shortest path from {start} to {end}: {' → '.join(path)} (Total: {total} km)")
else:
    print(f"No path from {start} to {end} found.")

"""
 
