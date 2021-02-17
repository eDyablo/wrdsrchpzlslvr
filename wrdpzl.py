def find_in_string(string, words):
    dictionary = words
    found = []
    begin, end = 0, 0
    while end <= len(string):
        word = string[begin:end]
        print(word)
        if word in dictionary:
            found.append(word)
            begin += len(word)
        end += 1
    return found


def make_prefix_table(words):
    table = {}
    for word in words:
        for size in range(1, len(word)):
            table[word[0:size]] = None
        table[word] = word
    return table
