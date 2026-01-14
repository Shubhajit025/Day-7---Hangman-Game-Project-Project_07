import random
import hangman_words
import hangman_art


lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

placeholder = ""
length_of_word = len(chosen_word)
for position in range(length_of_word):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_is_ended = False
display_list = []

while not game_is_ended:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in display_list:
        print(f"You've already guessed {guess}")
    display = ""

    for char in chosen_word:
        if char == guess:
            display += char
            display_list.append(guess)
        elif char in display_list:
            display += char
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_is_ended = True
            print(f"***********************IT WAS {chosen_word}!YOU LOSE**********************")

    if "_" not in display:
        game_is_ended = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
