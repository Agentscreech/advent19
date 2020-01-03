from helpers import *
data = get_input(3)
m = []
for line in data:
    m.append(line[:-1].split(","))
wire1 = m[0]
wire2 = m[1]

def go_right(disance, dx, dy, path):
    for _ in range(disance):
        dx += 1
        path.append((dx, dy))
    return dx, dy


def go_left(disance, dx, dy, path):
    for _ in range(disance):
        dx -= 1
        path.append((dx, dy))
    return dx, dy


def go_up(disance, dx, dy, path):
    for _ in range(disance):
        dy += 1
        path.append((dx, dy))
    return dx, dy


def go_down(disance, dx, dy, path):
    for _ in range(disance):
        dy -= 1
        path.append((dx, dy))
    return dx, dy


def get_path(wire):
    dx, dy = 0, 0
    path = []
    for move in wire:
        if move[0] == "R":
            dx, dy = go_right(int(move[1:]), dx, dy, path)
        if move[0] == "L":
            dx, dy = go_left(int(move[1:]), dx, dy, path)
        if move[0] == "U":
            dx, dy = go_up(int(move[1:]), dx, dy, path)
        if move[0] == "D":
            dx, dy = go_down(int(move[1:]), dx, dy, path)
    return path

intersections = set(get_path(wire1)).intersection(get_path(wire2))
dist = 999999999999999
for i in intersections:
    if i[0]+i[1] < dist:
        dist = i[0]+i[1]
print(dist)



