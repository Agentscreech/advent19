from helpers import *
data = get_input(1)

total = 0

def get_fuel(mass):
    return (mass//3)-2


for line in data:
    module_mass = int(line)
    sub_fuel = 0
    fuel = get_fuel(module_mass)
    while fuel >= 0:
        sub_fuel += fuel
        fuel = get_fuel(fuel)
    total += sub_fuel
print(total)

