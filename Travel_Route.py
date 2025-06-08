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