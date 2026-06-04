# Program to display water in the tank after each minute

water = 0
minute = 0

while water < 100:
    minute += 1
    water += 10
    print("After", minute, "minute(s), water in tank =", water, "liters")

print("Tank reached 100 liters.")