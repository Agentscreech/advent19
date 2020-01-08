from helpers import *
from collections import defaultdict, deque

class Node():
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name
        self.distance = None


planets = defaultdict()

data = get_input(6)

#build tree
for line in data:
    orbit = line[:-1].split(")")
    if orbit[0] not in planets:
        planets[orbit[0]] = Node(orbit[0])
    if orbit[1] not in planets:
        planets[orbit[1]] = Node(orbit[1])
    planets[orbit[0]].children.append(planets[orbit[1]])
    if planets[orbit[1]].parent is None:
        planets[orbit[1]].parent = planets[orbit[0]]

def get_distance(node):
    hops = 0
    first = node
    while node.parent:
        node = node.parent
        if node.distance:
            first.distance = hops + node.distance + 1
            return first.distance
        hops += 1
    first.distance = hops
    return hops

#BFS and count the number of hops from node to COM to get total indirect orbits
counter = 0
queue = deque([planets["COM"]])

while queue:
    planet = queue.pop()
    if planet.children:
        for child in planet.children:
            queue.append(child)
    counter += get_distance(planet)

print(counter)

