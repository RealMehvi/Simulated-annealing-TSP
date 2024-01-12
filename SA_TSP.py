import random
import math
import copy
import matplotlib.pyplot as plt

#########################################
############### Functions ###############
#########################################
# Generate random cities
def generate_random_cities(num_cities, x_range=(0, 100), y_range=(0, 100)):
  """Generates a list of random city coordinates within specified ranges."""
  cities = []
  for _ in range(num_cities):
    x = random.randint(*x_range)
    y = random.randint(*y_range)
    cities.append((x, y))
  return cities

# Function to calculate distance between two nodes
def distance(node1, node2):
  # Replace with your actual distance calculation here
  # This is a simple Euclidean distance for demonstration purposes
  return math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)

# Function to generate a random tour
def generate_random_tour(nodes):
  tour = list(range(len(nodes)))
  random.shuffle(tour)
  return tour

# Function to calculate the total distance of a tour
def tour_distance(tour, nodes):
  total_distance = 0
  for i in range(len(tour) - 1):
    node1 = nodes[tour[i]]
    node2 = nodes[tour[i + 1]]
    total_distance += distance(node1, node2)
  # Add distance from last city back to first city
  node1 = nodes[tour[-1]]
  node2 = nodes[tour[0]]
  total_distance += distance(node1, node2)
  return total_distance

# Simulated annealing algorithm for TSP
def simulated_annealing(nodes, initial_temperature, cooling_rate, iterations):
  # Generate a random initial tour
  temp_tour = generate_random_tour(nodes)
  temp_distance = tour_distance(temp_tour, nodes)

  # Main loop
  for i in range(iterations):
    # Generate a random neighbor tour
    neighbor_tour = temp_tour[:]
    random_i, random_j = random.sample(range(len(neighbor_tour)), 2)
    neighbor_tour[random_i], neighbor_tour[random_j] = neighbor_tour[random_j], neighbor_tour[random_i]

    # Calculate the distance of the neighbor tour
    neighbor_distance = tour_distance(neighbor_tour, nodes)

    # Calculate the energy difference (delta)
    delta = neighbor_distance - temp_distance

    # Accept the neighbor tour if it improves the distance or with a certain probability
    if delta < 0 or random.random() < math.exp(-delta / initial_temperature):
      temp_tour = neighbor_tour
      temp_distance = neighbor_distance

    # Cool down the temperature
    initial_temperature *= cooling_rate

  return temp_tour, temp_distance

#########################################
################ Instance ###############
#########################################

# Example
'''num_nodes = 50 # Adjust the number of cities as desired
nodes = generate_random_cities(num_nodes)'''

nodes = [(72, 81), (57, 32), (28, 33), (62, 0), (86, 66), (16, 99), (66, 90), (86, 27), (86, 91), (71, 82), (21, 80), (69, 55), (32, 1), (51, 69), (85, 41), (71, 18), (43, 9), (55, 70), (24, 48), (42, 18), (99, 18), (1, 27), (24, 5), (45, 25), (50, 66), (14, 65), (12, 2), (75, 45), (99, 67), (56, 13), (77, 35), (97, 15), (28, 40), (29, 15), (84, 98), (4, 51), (91, 37), (4, 76), (43, 42), (20, 11), (6, 82), (20, 14), (83, 11), (68, 21), (98, 11), (22, 92), (71, 84), (87, 15), (96, 82), (95, 44)]

initial_temperature = 100
cooling_rate = 0.99
iterations = 10000

best_solution, best_distance = simulated_annealing(nodes, initial_temperature, cooling_rate, iterations)

print("Best tour:", best_solution)
print("Best distance:", best_distance)


#########################################
############# Visualization #############
#########################################

# Plot the best solution
x = [nodes[i][0] for i in best_solution]
x.append(x[0])  # Add the first node again to close the loop
y = [nodes[i][1] for i in best_solution]
y.append(y[0])  # Add the first node again

plt.plot(x, y, '-o')  # Plot the tour as a line with markers
plt.xlabel("X-coordinates")
plt.ylabel("Y-coordinates")
plt.title("Best TSP Tour (Simulated Annealing)")
plt.show()
