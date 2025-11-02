import random

# Step 1: Generate a random number between 1 and 100
magic_number = random.randint(1, 100)

print("🔮 Welcome to the Fortune Teller's Magic Number Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

# Step 2: Start a loop for guesses
while True:
    guess = input("Enter your guess: ")

    # Make sure input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    # Step 3: Compare the guess to the magic number
    if guess < magic_number:
        print("Too low! 🌟 Try again.")
    elif guess > magic_number:
        print("Too high! 🌟 Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the magic number: {magic_number}")
        break  # Exit the loop when guessed correctly
