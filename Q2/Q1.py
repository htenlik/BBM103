year = int(input("Please enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("common year")
    else:
        print("leap year")
else:
    print("common year")
