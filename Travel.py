import tkinter as tk
from tkinter import messagebox, ttk
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



g = Graph()
g.add_route("Johannesburg", "Pretoria", 300)
g.add_route("Johannesburg", "Durban", 50)
g.add_route("Pretoria", "Polokwane", 200)
g.add_route("Cape Town", "Malawi", 2000)

def create_gui(graph):
    window = tk.Tk()
    window.title("Travel Route Planner")
    window.geometry("500x350")
    window.resizable(False, False)

    tk.Label(window, text="🚗 Travel Route Planner", font=("Arial", 16, "bold")).pack(pady=10)
    
    frame = tk.Frame(window)
    frame.pack(pady=10)

    cities = sorted(graph.routes.keys())

    tk.Label(frame, text="Start City:").grid(row=0, column=0, padx=5, pady=5)
    start_combo = ttk.Combobox(frame, values=cities, state="readonly")
    start_combo.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Destination City:").grid(row=1, column=0, padx=5, pady=5)
    end_combo = ttk.Combobox(frame, values=cities, state="readonly")
    end_combo.grid(row=1, column=1, padx=5, pady=5)

    result_text = tk.Text(window, height=8, width=58, state="disabled", bg="#f4f4f4")
    result_text.pack(pady=10)
    
    def find_route():
        start = start_combo.get()
        end = end_combo.get()

        if not start or not end:
                messagebox.showerror("Input Error", "Please select both start and destination cities.")
                return

        path, total = find_shortest_route(graph, start, end)
        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)

        if path is None:
            result_text.insert(tk.END, f"⚠️ No path found from {start} to {end}.\n")
        else:
            result_text.insert(tk.END, f"✅ Shortest route from {start} to {end}:\n")
            result_text.insert(tk.END, " → ".join(path) + f"\n🛣️ Total Distance: {total} km\n")

        result_text.config(state="disabled")
    tk.Button(window, text="Find Route", command=find_route, bg="#007acc", fg="white", width=20).pack()

    window.mainloop()
#Samanthas
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

    
    path, total_distance = find_shortest_route(graph, start, end)

    if path is None:
        print(f"⚠️  No path found from {start} to {end}.")
    else:
        print("\n✅ Route Found:")
        print(" -> ".join(path))
        print(f"🛣️  Total Distance: {total_distance} km\n")


create_gui(g)