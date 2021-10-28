z = ""
while z != "end":
    N = int(input("skriv ett numer mellan 2 och 40: "))
    if N < 2 or N > 40:
        print("inte ett numer mellan 1 och 40")
    else:
        poglist = 0
        y = 1
        for x in range(0, N):
            pog = pow(y, 3)
            poglist += pog
            y += 1
        print(poglist)


    z = input("type end to end: ")