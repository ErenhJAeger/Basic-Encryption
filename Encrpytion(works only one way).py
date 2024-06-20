import string
import random

# making a list of all the letters,number and characters using the String library
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()


# shuffling the elements in key to create the encrypted message
random.shuffle(keys)

# ENCRYPTION
plain_text = input("Hello!, Type the message you wanna encrypt: \n")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += keys[index]
print(f"encrypted message: \n {cypher_text}")
