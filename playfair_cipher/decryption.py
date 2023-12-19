import encryption


def playfair_decryption(key, message):
    plaintext = encryption.playfair_encryption(key, message, -1)

    return plaintext
