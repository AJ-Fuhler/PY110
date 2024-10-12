def swap(string):
    if len(string) == 1:
        return string
    
    words = string.split()
    for idx in range(len(words)):
        if len(words[idx]) == 1:
            continue

        word = list(words[idx])
        first_char = word.pop(0)
        last_char = word.pop(-1)
        word.insert(0, last_char)
        word.append(first_char)
        words[idx] = ''.join(word)
    
    result = ' '.join(words)
    return result



def swap(string):
    words = string.split()
    for idx in range(len(words)):
        words[idx] = swap_first_last_char(words[idx])

    return ' '.join(words)

def swap_first_last_char(word):
    if len(word) == 1:
        return word
    
    return word[-1] + word[1:-1] + word[0]



print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

