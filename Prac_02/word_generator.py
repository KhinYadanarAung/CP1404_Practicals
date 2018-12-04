import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

"""
word_format = "ccvcvvc"
word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
"""

#Use wildcards for the vowels (#) and consonants (%) or either (*) and make alphabetical characters use that actual character - e.g. the format “%re#*l*” might produce a word like “greatly” or “breuzla”

word_format = input("Enter word format\n(#) - vowels\n(%) - consonants\neither(*)")
word = ""

for kind in word_format.lower():
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(CONSONANTS+VOWELS)
    else:
        word += kind
        
print(word)
"""
#Automatically (randomly) generate the word_format variable
word_format = ""
word = ""
for i in range (5):
    word_format += random.choice("cv")

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
"""