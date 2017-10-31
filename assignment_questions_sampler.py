# Generates random practice questions from a set of chapters and questions
import random

def choose(start = 1, end = 10, num = 5):
    if num > end - start  + 1:
        num = end - start + 1
        
    return random.sample(range(start, end + 1), num)


# Main
done = False

questions = [(1, 5),
             (2, 5),
             (3, 5),
             (4, 5),
             (5, 5)]

total = 0
for item in questions:
    total += item[1]

while not done:
    print("=================================================")
    n = int(input("How many (max: " + str(total) + "): "))
    res = []
    for item in questions:
        for i in range(1, item[1] + 1):
            res.append((item[0], i))

    random.shuffle(res)
    for i in range(n):
        print(res[i])

    i = input("Press 'Y' to go again ")
    if (i != 'Y' and i != 'y'):
        done = True

