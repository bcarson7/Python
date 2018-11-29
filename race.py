import random

first_lap = 0

def race(laps):
    total = 0
    race = 0
    for i in range(laps):
        first_lap = round(random.uniform(100, 150),3)
        total += first_lap
        race = round((total/laps),3)
        print(first_lap)
    print("Race Speed: " + str(race))

print('U-1')
race(3)

print('')
print('U-9')
race(3)
