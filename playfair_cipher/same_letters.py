# Add fillers if the same letter is in a pair
def separate_same_letters(message):
    index = 0
    while index < len(message):
        first_letter = message[index]
        if index == len(message) - 1:
            message = message + 'X'
            index += 2
            continue
        second_letter = message[index + 1]
        if first_letter == second_letter:
            message = message[:index + 1] + "X" + message[index + 1:]
        index += 2
    return message
