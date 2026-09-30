import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Create blanks
guessed_word = ["_"] * len(word)

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

# Store guessed letters
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(guessed_letters))
    
    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in word
    if guess in word:
        print("Correct guess! ✅")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess! ❌")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# Result
if "_" not in guessed_word:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n😢 Game Over!")
    print("The correct word was:", word)
