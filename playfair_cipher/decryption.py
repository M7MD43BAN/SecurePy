from playfair_cipher.encryption import playfair_encryption


def playfair_decryption(key, message):
    plaintext = playfair_encryption(key, message, inc=-1)

    return plaintext
