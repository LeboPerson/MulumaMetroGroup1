#This is the Advanced Project 6
#I will send project responsibilities

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
g.add_route("Pretoria", "Polokwane", 200)
g.add_route("Cape Town", "Malawi", 2000)
  
#for city, neighbors in g.routes.items():
 #   print(f"{city} connected to: {neighbors}")


 # Samantha's Code
def travel_interface(graph):
    print("🚗 Welcome to the Travel Route Planner!")
    print("📍 Available Cities:", ", ".join(graph.routes.keys()))

    start = input("Enter starting city: ").strip().title()
    end = input("Enter destination city: ").strip().title()

    if start not in graph.routes:
        print(f"4😵4 Error: '{start}' not found in city list.")
        return
    if end not in graph.routes:
        print(f"4😵4 Error: '{end}' not found in city list.")
        return

    previous, distances = find_shortest_route(graph, start, end)
    path, total_distance = reconstruct_path(previous, distances, start, end)

    if path is None:
        print(f"⚠️  No path found from {start} to {end}.")
    else:
        print("\n✅ Route Found:")
        print(" -> ".join(path))
        print(f"🛣️  Total Distance: {total_distance} km\n")