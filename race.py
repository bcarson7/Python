import random

user = input('Enter the the number of laps')
user = int(user)

def race(laps):
    total = 0
    for i in range(laps):
        race_lap = round(random.uniform(100, 150),3)
        total += race_lap
        heat = round((total/laps), 3)
        print(race_lap)
    print("AVG: " + str(heat) + " MPH")

print('U-1')
race(user)

print('')
print('U-9')
race(user)
