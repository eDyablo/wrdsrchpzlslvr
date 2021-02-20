from grid import Grid


class Hunter:
    def __init__(self, words):
        self.__table = make_prefix_table(words)

    def find_in_string(self, string):
        dictionary = self.__table
        found = []
        begin, end = 0, 0
        while end <= len(string):
            while begin < end and string[begin:end] not in dictionary:
                begin += 1
            for left in range(begin, end):
                word = string[left:end]
                if word in dictionary and dictionary[word]:
                    found.append(word)
            end += 1
        return found


def make_prefix_table(words):
    table = {}
    for word in words:
        for size in range(1, len(word)):
            prefix = word[0:size]
            if prefix not in table:
                table[prefix] = None
        table[word] = word
    return table


class Board(Grid):
    @staticmethod
    def load(data):
        board = Board()
        for row, record in enumerate(data):
            for column, item in enumerate(record):
                board[row, column] = item
        return board


def solve(board, words):
    hunter = Hunter(words)
    found = []
    row_count, column_count = board.size()
    for row in range(0, row_count):
        found.extend(hunter.find_in_string(
            ''.join(map(str, board.iterate((row, 0), Grid.RIGHTWARD)))))
    for column in range(0, column_count):
        found.extend(hunter.find_in_string(
            ''.join(map(str, board.iterate((0, column), Grid.DOWNWARD)))))
    return found
