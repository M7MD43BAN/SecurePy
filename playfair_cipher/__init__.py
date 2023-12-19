from encryption import playfair_encryption
from decryption import playfair_decryption

if __name__ == "__main__":
    plaintext = "Hello Everyone"
    key = "secret"
    print("Plain Text is : " + plaintext)
    print("Key is : " + key)
    ciphertext = playfair_encryption(key, plaintext)
    print("Cipher Text is : " + ciphertext)
    print("Decrypted Text is : " + playfair_decryption(key, ciphertext))
