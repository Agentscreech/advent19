from helpers import get_input

data = get_input(8)
for line in data:
    image = line[:-1]

# image = "123456789012"

#build the layers
def build_layers(row, col):
    layers = []
    start = 0
    end = row * col 
    for i in range((row*col)-1,len(image), row*col):
        layers.append(image[start:end])
        start = i+1
        end = start + (row * col)
    return layers

layers = build_layers(25, 6)

#for each layer, count the 0s
zero_counts = list(map(lambda x: x.count("0"), layers))
#find the smallest counts
layer = layers[zero_counts.index(min(zero_counts))]
#in layer with fewest 0's, print count 1 * count 2
print(layer.count("1") * layer.count("2"))



