def monoalphabetic_decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    plaintext = ''

    for character in ciphertext:
        if character.isalpha():
            # Use the key for the corresponding case
            plaintext += chr(key.index(character) + ord('a'))
        else:
            plaintext += character  # Keep non-alphabetic characters unchanged

    return plaintext
