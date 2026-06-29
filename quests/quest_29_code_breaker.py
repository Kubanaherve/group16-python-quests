secret = 42
attempts = 3

while attempts > 0:
    guess = int(input("Guess the code: "))

    if guess == secret:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Locked out!")
