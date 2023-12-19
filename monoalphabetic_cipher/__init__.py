from decryption import monoalphabetic_decrypt
from encryption import monoalphabetic_encrypt

if __name__ == "__main__":
    plaintext = "HELLO EVERYONE"
    print("Plain Text is : " + plaintext)
    ciphertext, key = monoalphabetic_encrypt(plaintext)
    print("Cipher Text is : " + ciphertext)
    print("Key is : " + key)
    print("Decrypted Text is : " + monoalphabetic_decrypt(ciphertext, key))
