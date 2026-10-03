import random

print("===== NUMBER GUESSING GAME =====")

# Computer chooses a random number
secret_number = random.randint(1, 100)

attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        
        elif guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\n🎉 Congratulations!")
            print("You guessed the correct number!")
            print("The number was:", secret_number)
            print("Attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")