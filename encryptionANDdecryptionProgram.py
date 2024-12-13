import random
import string

def generate_key():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def encrypt(plain_text, chars, key):
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # Keep unknown characters unchanged
    return cipher_text

def decrypt(cipher_text, chars, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter  # Keep unknown characters unchanged
    return plain_text

chars, key = generate_key()

# Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt(plain_text, chars, key)
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decryption
cipher_text = input("Enter a message to decrypt: ")
plain_text = decrypt(cipher_text, chars, key)
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
