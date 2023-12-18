def caesar_cipher_encryption(plaintext, shift):
    ciphertext = ""
    # iterate over the given plaintext
    for i in range(len(plaintext)):
        # get the character from the plaintext
        character = plaintext[i]
        # check if space is there then simply add space
        if character == " ":
            ciphertext += " "
        # check if a character is uppercase then encrypt it accordingly
        elif character.isupper():
            ciphertext += chr((ord(character) + shift - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        elif character.islower():
            ciphertext += chr((ord(character) + shift - 97) % 26 + 97)

    return ciphertext
