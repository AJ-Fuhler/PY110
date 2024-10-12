def clear_word(word):
    cleared_word = ''
    for char in word:
        if char.isalpha():
            cleared_word += char
    
    return cleared_word

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        word_size = len(clear_word(word))
        if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1

    return counts

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})