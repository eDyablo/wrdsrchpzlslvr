#!/usr/bin/env python3

from argparse import ArgumentParser
from operator import add
from random import choice as choice_from
from re import split


class Grid:
    DOWNWARD = (1, 0)
    LEFTWARD = (0, -1)
    RIGHTWARD = (0, 1)
    UPWARD = (-1, 0)
    DIAGONALLY_DOWN_LEFT = tuple(map(add, DOWNWARD, LEFTWARD))
    DIAGONALLY_DOWN_RIGHT = tuple(map(add, DOWNWARD, RIGHTWARD))
    DIAGONALLY_UP_LEFT = tuple(map(add, UPWARD, LEFTWARD))
    DIAGONALLY_UP_RIGHT = tuple(map(add, UPWARD, RIGHTWARD))

    def __init__(self):
        self.__cells = dict()
        self.__size = 0, 0

    def cell_count(self):
        return len(self.__cells)

    def size(self):
        return self.__size

    def iterate(self, begin, direction):
        cursor = begin
        while cursor in self:
            yield self[cursor]
            cursor = tuple(map(add, cursor, direction))

    def values(self):
        return self.__cells.values()

    def __setitem__(self, key, value):
        row, column = key
        index = self.__index(row, column)
        self.__cells[index] = value
        self.__size = max(self.__size[0], row +
                          1), max(self.__size[1], column + 1)

    def __getitem__(self, key):
        index = self.__index(*key)
        return self.__cells[index] if index in self.__cells else None

    def __index(self, row, column):
        return f'{row}x{column}'

    def __contains__(self, key):
        row, column = key
        row_count, column_count = self.size()
        return (0 <= row < row_count) and (0 <= column < column_count)


class Hunter:
    def __init__(self, words):
        self.__table = make_prefix_table(words)

    def find(self, string):
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

    @staticmethod
    def random(sequence, size):
        board = Board()
        if len(sequence):
            row_count, column_count = size
            for row in range(0, row_count):
                for column in range(0, column_count):
                    board[row, column] = choice_from(sequence)
        return board

    def letters(self):
        return self.values()

    def __str__(self):
        row_count, _ = self.size()
        return'\n'.join([' '.join(map(str, self.iterate((row, 0), self.RIGHTWARD)))
                         for row in range(0, row_count)])


class Solver:
    def __init__(self, words):
        self.__hunter = Hunter(words)

    def solve(self, board):
        hunter = self.__hunter
        found = []
        row_count, column_count = board.size()
        for row in range(0, row_count):
            rightward = ''.join(
                map(str, board.iterate((row, 0), Grid.RIGHTWARD)))
            found.extend(hunter.find(rightward))
            found.extend(hunter.find(rightward[::-1]))
            down_right = ''.join(map(str, board.iterate(
                (row, 0), Grid.DIAGONALLY_DOWN_RIGHT)))
            found.extend(hunter.find(down_right))
            found.extend(hunter.find(down_right[::-1]))
            up_right = ''.join(map(str, board.iterate(
                (row + 1, 0), Grid.DIAGONALLY_UP_RIGHT)))
            found.extend(hunter.find(up_right))
            found.extend(hunter.find(up_right[::-1]))
        for column in range(0, column_count):
            downward = ''.join(
                map(str, board.iterate((0, column), Grid.DOWNWARD)))
            found.extend(hunter.find(downward))
            found.extend(hunter.find(downward[::-1]))
            down_right = ''.join(map(str, board.iterate(
                (0, column + 1), Grid.DIAGONALLY_DOWN_RIGHT)))
            found.extend(hunter.find(down_right))
            found.extend(hunter.find(down_right[::-1]))
            up_right = ''.join(map(str, board.iterate(
                (row_count - 1, column + 1), Grid.DIAGONALLY_UP_RIGHT)))
            found.extend(hunter.find(up_right))
            found.extend(hunter.find(up_right[::-1]))
        return found


def argparser():
    parser = ArgumentParser(
        description="Words search puzzle solver"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument('-r', '--random', dest='random_size', default='15x15',
                        help='random board size, default is 15x15')
    parser.add_argument('-w', '--words', dest='words_file', default='words.txt',
                        help='file contains words, default is ./words.txt')
    parser.add_argument('-l', '--letters', default='abcdefghijklmnopqrstuvwxyz',
                        help='sequence of letters')
    parser.add_argument('--no-board', dest='show_board',
                        action='store_false', default=True, help='do not show board')
    parser.add_argument('--no-words', dest='show_found',
                        action='store_false', default=True, help='do not show found words')
    parser.add_argument('--count', dest='show_count', action='store_true',
                        default=False, help='show count of found words')
    return parser


def load_words(path):
    try:
        with open(path) as file:
            return list(map(str.strip, file.readlines()))
    except:
        return []


def parse_size(text):
    text = text.strip()
    if not text:
        return (0, 0)
    try:
        s = int(text)
        return (s, s)
    except:
        return tuple(map(int, split(r'\s*\D\s*', text, 2)))


def main():
    args = argparser().parse_args()

    board = Board.random(args.letters, parse_size(args.random_size))

    print(board) if args.show_board and board.letters() else None

    words = load_words(args.words_file)

    found = Solver(words).solve(board)

    print(len(found)) if args.show_count else None
    print(*found) if found and args.show_found else None


if __name__ == "__main__":
    main()
