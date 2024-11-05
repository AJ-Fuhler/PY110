def word_to_digit(message):
    word_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    split_message = message.split()
    for idx in range(len(split_message)):
        if split_message[idx] in word_number:
            split_message[idx] = word_number[split_message[idx]]

    
    return ' '.join(split_message)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True