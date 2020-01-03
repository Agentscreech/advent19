from helpers import *
import collections
data = get_input(4)
for line in data:
    r = line.split("-")
    start = int(r[0])
    end = int(r[1])
data.close()

def has_doubles(n):
    #only valid if there is a single pair of numbers, any more or less is invald
    return 2 in collections.Counter(n).values()

def isInOrder(num):
    return num == ''.join(sorted(num))

count = 0
while start < end:
    #check if it's in acending order and if it's got a duplicate
    if isInOrder(str(start)) and has_doubles(str(start)):
        count += 1
    start += 1

print(count)
