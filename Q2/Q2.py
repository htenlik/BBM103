print("roots for x^2+bx+c")
b = int(input("give the b value: "))
c = int(input("give the c value: "))
delta = (b**2)-4*c
if delta >= 0:
    x1 = (-b-delta**0.5)/2
    x2 = (-b+delta**0.5)/2
    print("roots are:")
    print(x1)
    print(x2)
else:
    print("there is no reel root in this case")
