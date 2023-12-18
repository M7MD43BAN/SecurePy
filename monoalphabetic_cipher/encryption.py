import cipher_key


def monoalphabetic_encrypt(plaintext):
    plaintext = plaintext.lower()
    key = cipher_key.generate_key()
    ciphertext = ''

    for character in plaintext:
        if character.isalpha():
            # Use the key for the corresponding case
            ciphertext += key[ord(character) - ord('a')]
        else:
            ciphertext += character  # Keep non-alphabetic characters unchanged

    return ciphertext, key
