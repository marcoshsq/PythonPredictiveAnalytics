import random
from words import words
import string
from visuals import lives_visual_dict


def valid_word(words):
    word = random.choice(words)  # Escolhe uma palavra do outro arquivo
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = valid_word(words)
    word_letters = set(word)  # Letras ná variável word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Para registrar as letras do user

    lives = 7

    # Recebendo dados do user
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(
            "You have",
            lives,
            "lives left and you have used these letters: ",
            " ".join(used_letters),
        )

        # Qual a palavra certa
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")

            else:
                lives = lives - 1  # Perde uma vida u.u
                print("\nYour letter,", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print("\nYou have already used that letter. Guess another letter.")

        else:
            print("\nPlease enter a valid character!")

    # Se o jogador perder
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the correct word", word, "!")


if __name__ == "__main__":
    hangman()
