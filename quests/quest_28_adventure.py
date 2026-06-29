def start():
    choice = input("You are in a forest. Go left or right? ")

    if choice == "left":
        cave()
    else:
        river()

def cave():
    print("You found treasure!")

def river():
    print("You were caught by a monster!")

start()
