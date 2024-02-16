import numpy as np

from tbrankovic.utils.convert_text_to_binary import convert_text_to_binary


def generate_stream(message_type: str, size: int, message=None):
    message_type = message_type.lower()

    stream = None

    if message_type == "alternating":
        # generate stream of alternating 1s and 0s
        stream = np.array([0, 1] * (size // 2))
        stream = stream[:size]

    elif message_type == "custom" and message is not None:
        # convert the input message to binary stream
        binary_message = convert_text_to_binary(message)

        # check if there is no message
        if len(message) == 0:
            stream = np.zeros(size)
        else:
            repetitions = int(np.ceil(size / len(binary_message)))
            stream = np.tile(binary_message, repetitions)
            stream = stream[:size]

    else:  # message_type == "random":
        # generate random stream of 1s and 0s
        stream = np.random.randint(0, 2, size=size)

    return stream

# print(generate_stream("custom", 50, "a"))
