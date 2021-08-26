x = ""

while x != "y":
    text = input("skriv: ").lower()
    emptyText = ""


    konsonanter = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "z", "x"]


    for A in text:
        if (A in konsonanter):
            emptyText += (A + "o" + A)
        else:
            emptyText += A
    

    print(emptyText)
    x = input("end?: ")
