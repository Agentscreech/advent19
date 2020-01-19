from helpers import get_input

data = get_input(8)
for line in data:
    image = line[:-1]

# image = "0222112222120000"

#build the layers


# end_result = [
#     layer [row[0,2],row[2,2]],
#     [1,1,2,2],
#     [2,2,1,2],
#     [0,0,0,0]
#     ]

def build_layers(row, col):
    pointer = 0
    layers = []
    while pointer < len(image):
        layer, pointer = build_column(col, row, pointer)
        layers.append(layer)
    return layers

def build_column(col, row, pointer):
    c = []
    for _ in range(col):
        column, pointer = build_row(row, pointer)
        c.append(column)
    return c, pointer

def build_row(row, pointer):
    r = []
    for _ in range(row):
        r.append(image[pointer])
        pointer += 1
    return r, pointer

def resolve_image(layers, row, col):
    image = [[0 for x in range(row)] for y in range(col)]
    for r in range(row):
        for c in range(col):
            for layer in layers:
                if layer[c][r] == "2":
                    continue
                else:
                    image[c][r] = layer[c][r]
                    break
    return image


def render_image(image):
    for line in image:
        print("")
        for pixel in line:
            #the 1's are pixels in ASCII text image, 0's are blank spaces.  
            print(pixel.replace("0", " "), end="")


layers = build_layers(25, 6)
i = resolve_image(layers, 25, 6)
render_image(i)

