x = int(input("how many numbers do you want to check (1-20)"))

antal = []

if 1 <= x <= 20:
    print("Bassed")
    while x > 0:
        print(x)
        antal.append(x)
        x -= 1

else:
    print("Not pog")