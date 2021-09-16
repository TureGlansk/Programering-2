def food(s, vegan=False):
    if (vegan):
        print("Fake" + s)
    else:
        print(s)
food("Mjölk", True)
food("Mjölk")