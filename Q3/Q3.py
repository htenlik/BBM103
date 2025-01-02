import random
number = random.randint(1,25)
guess = int(input("guess it"))

while guess != random:
    if guess<number:
        print("give me higher value")
        guess = int(input("one more shot"))
    elif guess>number:
        print("give me lower value")
        guess = int(input("one more shot"))
    else:
        print("congratz")
        break
