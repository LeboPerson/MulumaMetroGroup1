
from Travel_Route import Graph
from collections import deque

def find_shortest_route(graph, start, end):
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

    # Path created for test purposes

    # path = []
    # city = end
    # while city:
    #     path.insert(0, city)
    #     city = previous[city]

    # if distances[end] == float('inf'):
    #     return None, None
    # return path, distances[end]

# 
# 
# Display if the code works with given paremeters from the Travel_Route
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