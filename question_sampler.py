# Generates a random subset of a list of numbers
import random

def choose(start = 1, end = 10, num = 5):
    if num > end - start  + 1:
        num = end - start + 1
        
    return random.sample(range(start, end + 1), num)


# Main
done = False
while not done:
    print("=================================================")
    s = int(input("Start: "))
    e = int(input("End: "))
    n = int(input("How many (max: " + str(e - s + 1) + "): "))

    res = choose(s, e, n)
    res.sort()
    print(res)

    i = input("Press 'Y' to go again ")
    if (i != 'Y' and i != 'y'):
        done = True

