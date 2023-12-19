from decryption import caesar_cipher_decryption
from encryption import caesar_cipher_encryption

if __name__ == '__main__':
    plaintext = "HELLO EVERYONE"
    key = 3
    print("Plain Text is : " + plaintext)
    print("Shift pattern is : " + str(key))
    ciphertext = caesar_cipher_encryption(plaintext, key)
    print("Cipher Text is : " + ciphertext)
    print("Decrypted Text is : " + caesar_cipher_decryption(ciphertext, key))
