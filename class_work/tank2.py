# Program to display water level in a tank

water = 0
minute = 0

while water < 100:
    minute += 1
    water += 10
    print("After", minute, "minute(s), water in tank =", water, "liters")

print("Tank reached 100 liters and is full.")