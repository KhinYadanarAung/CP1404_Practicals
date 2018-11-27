import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
def main():
    word_format = input("Enter word format\n(v) - vowels\n(c) - consonants")
    while not is_valid_format(word_format):
        print("Invalid word format")
        word_format = input("Enter word format\n(v) - vowels\n(c) - consonants")

    word = ""

    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)

def is_valid_format(word_format):
    word_format = word_format.lower()
    count = 0
    is_valid = True
    while is_valid and count < len(word_format):
        if word_format[count] == "c" or word_format[count] == "v":
            pass
        else:
            is_valid = False

        count += 1

    return is_valid

main()