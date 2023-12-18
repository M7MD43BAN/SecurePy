import encryption


def caesar_cipher_decryption(ciphertext, shift):
    # Call the encryption function with a negative shift to decrypt
    return encryption.caesar_cipher_encryption(ciphertext, -shift)
