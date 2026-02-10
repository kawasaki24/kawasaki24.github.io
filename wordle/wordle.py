import random

def load_random_word(filename="words.txt"):
    with open(filename) as file:
        return random.choice(file.read().splitlines())

def evaluate_guess(guess, word, misplaced, incorrect):
    result = []

    for g, w in zip(guess, word):
        # correct letter, correct position
        if g == w:
            result.append(g)
            misplaced.discard(g)
            incorrect.discard(g)

        # correct letter, wrong position (misplaced letter)
        elif g in word:
            result.append("_")
            misplaced.add(g)
            
        # incorrect letter
        else:
            result.append("_")
            incorrect.add(g)
    
    print("".join(result))

    if misplaced: 
        print("Misplaced letters: " + ", ".join(sorted(misplaced)))
    if incorrect: 
        print("Incorrect lettters: " + ", ".join(sorted(incorrect)))

def main():
    word = load_random_word()
    misplaced_letters = set()
    incorrect_letters = set()

    for attempt in range(0, 5):
        print(f"You have {5 - attempt} guesses left")
        guess = input("Guess a 5-letter word: ").lower()

        if len(guess) != len(word) or not guess.isalpha():
            print("Guess must be 5 letters long and alphabetical letters")
            continue

        if guess == word:
            print("Correct!")
            return
        
        evaluate_guess(guess, word, misplaced_letters, incorrect_letters)

    print(f"No more chances! The word was {word}")




if __name__ == "__main__":
    main()