import numpy as np


def convert_text_to_binary(text: str):
    binary_message = ''.join(format(ord(char), '08b') for char in text)
    print(text, binary_message)

    return np.array([int(bit) for bit in binary_message])
