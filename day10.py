from helpers import get_input

# data =  ".#..#\n.....\n#####\n....#\n...##"
data = get_input(10)
#make 2d array of the 'map'
field = []
for line in data:
    field.append([x for x in line[:-1]])


asteroid_locations = {}

class Node():
    def __init__(self, loc):
        self.loc = loc
        self.x, self.y = get_coords(loc)
        self.total = 0

def find_asteroids():
    #f[y][x]
    #iterate left to right of the 2d array.  When you find an asteroid, make it the root.
    for y, _ in enumerate(field):
        for x, space in enumerate(field[y]):
            if space == "#":
                location = f"{x}, {y}"
                asteroid_locations[location] = Node(location)

def get_coords(loc):
    temp = loc.split(", ")
    return int(temp[0]), int(temp[1])

def find_right_blocked(ast: Node):
    #find all things to the right of current nodes x coord
    b = 0
    for x in range(ast.x+1,len(field[0])):
        name = f"{x}, {ast.y}"
        if name in asteroid_locations:
            b += 1
            break
    return b

def find_left_blocked(ast):
    b = 0
    for x in range(ast.x-1, -1, -1):
        name = f"{x}, {ast.y}"
        if name in asteroid_locations:
            b += 1
            break
    return b

def find_down_blocked(ast):
    b = 0
    for y in range(ast.y+1, len(field)):
        name = f"{ast.x}, {y}"
        if name in asteroid_locations:
            b += 1
            break
    return b

def find_up_blocked(ast):
    b = 0
    for y in range(ast.y-1, -1, -1):
        name = f"{ast.x}, {y}"
        if name in asteroid_locations:
            b += 1
            break
    return b

def find_up_left_blocked(dx, dy, ast):
    b = 0
    x = ast.x
    y = ast.y
    while x > -1 and y > -1:
            name = f"{x+dx}, {y+dy}"
            if name in asteroid_locations:
                b += 1
                break
            x += dx
            y += dy
    return b

def find_up_right_blocked(dx, dy, ast):
    b = 0
    x = ast.x
    y = ast.y
    while x < len(field[0]) and y > -1:
            name = f"{x+dx}, {y+dy}"
            if name in asteroid_locations:
                b += 1
                break
            x -= dx
            y += dy
    return b

def find_down_left_blocked(dx, dy, ast):
    b = 0
    x = ast.x
    y = ast.y
    while x > -1 and y < len(field):
            name = f"{x+dx}, {y+dy}"
            if name in asteroid_locations:
                b += 1
                break
            x += dx
            y += dy
    return b

def find_down_right_blocked(dx, dy, ast):
    b = 0
    x = ast.x
    y = ast.y
    while x < len(field[0]) and y < len(field):
        name = f"{x+dx}, {y + dy}"
        if name in asteroid_locations:
            b += 1
            break
        x += dx
        y += dy
    return b

find_asteroids()

def find_max_seen():
    m = 0
    for a1 in asteroid_locations:
        ast1 = asteroid_locations[a1]
        ast1.total = len(asteroid_locations)-1
        for a2 in asteroid_locations:
            if a1 is not a2:
                ast2 = asteroid_locations[a2]
                if abs(ast2.x - ast1.x) == abs(ast2.y - ast1.y):
                    dx = (ast2.x - ast1.x)//abs(ast2.y - ast1.y)
                    dy = (ast2.y - ast1.y)//abs(ast2.x - ast1.x)
                else:
                    dx = ast2.x - ast1.x
                    dy = ast2.y - ast1.y

                #it's a cardnal direction
                if ast1.x < ast2.x and ast1.y == ast2.y:
                    #it's to the right
                    ast1.total -= find_right_blocked(ast2)
                    continue
                if ast1.x > ast2.x and ast1.y == ast2.y:
                    #it's to the left
                    ast1.total -= find_left_blocked(ast2)
                    continue
                if ast1.y < ast2.y and ast1.x == ast2.x:
                    #it's below
                    ast1.total -= find_down_blocked(ast2)
                    continue
                if ast1.y > ast2.y and ast1.x == ast2.x:
                    #it's above
                    ast1.total -= find_up_blocked(ast2)
                    continue
                #diagonals
                if dx < 0 and dy > 0:
                    #down and left
                    ast1.total -= find_down_left_blocked(dx, dy, ast2)
                    continue
                if dx > 0 and dy > 0:
                    #down and right
                    ast1.total -= find_down_right_blocked(dx, dy, ast2)
                    continue
                if dx < 0 and dy < 0:
                    #up and left
                    ast1.total -= find_up_left_blocked(dx, dy, ast2)
                    continue
                if dx > 0 and dy < 0:
                    #up and right
                    ast1.total -= find_up_right_blocked(dx, dy, ast2)
                    continue
        if m < ast1.total:
            m = ast1.total
    return m

print(find_max_seen())




# from root asteroid, when you find an asteroid, find all asteroids that are in the same path it took to reach from root within bounds of map.
# subtract all of those found from the total and set that as the number of asteroids it can "see" including itself

# find the asteroid that can see the most and return how many it can see

