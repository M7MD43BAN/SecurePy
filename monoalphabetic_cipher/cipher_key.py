import random
import string


def generate_key():
    # Function to generate a random monoalphabetic key
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)
