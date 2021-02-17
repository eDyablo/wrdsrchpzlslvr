def find_in_string(string, words):
    dictionary = make_prefix_table(words)
    found = []
    begin, end = 0, 0
    while end <= len(string):
        word = string[begin:end]
        if word in dictionary and dictionary[word]:
            found.append(word)
            begin += len(word)
        else:
            while begin < end and string[begin:end] not in dictionary:
                begin += 1
        end += 1
    return found


def make_prefix_table(words):
    table = {}
    for word in words:
        for size in range(1, len(word)):
            table[word[0:size]] = None
        table[word] = word
    return table
