direction = input("Go left or right? ").lower()
if direction == "left":
    action = input("Do you swim or wait? ").lower()
    if action == "swim":
        print("You found treasure!")
    else:
        print("You waited and found nothing.")
else:
    print("You found a sleeping dragon and snuck away.")
