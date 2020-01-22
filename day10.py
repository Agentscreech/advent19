

data =  ".#..#\n.....\n#####\n....#\n...##"

#make 2d array of the 'map'
field = []
for line in data.split('\n'):
    field.append([x for x in line])


a = {}

class Node():
    def __init__(self, loc):
        self.loc = loc

def find_asteroid():
    # x = 0
    # y = 0
    w = len(field[0])
    h = len(field)
    #f[y][x]
# iterate left to right of the 2d array.  When you find an asteroid, make it the root.
    for y, _ in enumerate(field):
        for x, space in enumerate(field[y]):
            if space == "#":
                location = f"({x}, {y})"
                a[location] = Node(location)
    print(a)

find_asteroid()




# from root asteroid, when you find an asteroid, find all asteroids that are in the same path it took to reach from root within bounds of map.
# subtract all of those found from the total and set that as the number of asteroids it can "see" including itself

# find the asteroid that can see the most and return how many it can see

