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

# build tree
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
            #we know the distance of it's parent, so don't need to continue
            first.distance = hops + node.distance + 1
            return first.distance
        hops += 1
    first.distance = hops
    return hops

def find_orbits(planets):
    # BFS and count the number of hops from node to COM to get total indirect orbits
    counter = 0
    queue = deque([planets["COM"]])

    while queue:
        planet = queue.pop()
        if planet.children:
            for child in planet.children:
                queue.append(child)
        counter += get_distance(planet)
    return counter

def get_path(node):
    path = []
    while node.parent:
        node = node.parent
        path.append(node.name)
    return path

def find_intersection(node, santa_path):
    path = []
    while node.name not in santa_path:
        node = node.parent
        path.append(node.name)
    return path, node.name

def find_transfers(planets):
    #map path from santa to com
    santa_path = get_path(planets["SAN"])
    #find the common planet
    path, intersection = find_intersection(planets["YOU"], santa_path)
    #add the path length from common planet to santa + comment planet to you
    return len(santa_path[:santa_path.index(intersection)]) + len(path[:path.index(intersection)])


print(find_orbits(planets), "total indirect orbits")
print(find_transfers(planets), "total transfers to Santa")