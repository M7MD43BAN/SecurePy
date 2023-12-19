import playfair_matrix
import same_letters


# Return the index of a letter in the matrix
# This will be used to know what rule (1-4) to apply
def indexOf(letter, matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return i, index
        except:
            continue


def playfair_encryption(key, message, inc=1):
    matrix = playfair_matrix.create_matrix(key)
    message = message.upper()
    message = message.replace(' ', '')
    message = same_letters.separate_same_letters(message)
    cipher_text = ''

    for (first_letter, second_letter) in zip(message[0::2], message[1::2]):
        row1, col1 = indexOf(first_letter, matrix)
        row2, col2 = indexOf(second_letter, matrix)

        if row1 == row2:  # Rule 2, the letters are in the same row
            cipher_text += matrix[row1][(col1 + inc) % 5] + matrix[row2][(col2 + inc) % 5]
        elif col1 == col2:  # Rule 3, the letters are in the same column
            cipher_text += matrix[(row1 + inc) % 5][col1] + matrix[(row2 + inc) % 5][col2]
        else:  # Rule 4, the letters are in a different row and column
            cipher_text += matrix[row1][col2] + matrix[row2][col1]

    return cipher_text
