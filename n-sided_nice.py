# Rolls an n-sided dice any number of times
import random

# Main
done = False
while not done:
    print("=================================================")
    s = int(input("Sides: "))
    e = int(input("How many times: "))

    if s < 2: s = 2
    for i in range(0, e):
        print(random.randint(1, s))

    i = input("Press 'Y' to go again ")
    if (i != 'Y' and i != 'y'):
        done = True

