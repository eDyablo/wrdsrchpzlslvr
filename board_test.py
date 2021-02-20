from functools import reduce
from operator import mul
from pytest import (fixture, mark)
from wrdpzl import Board


@fixture
def board():
    return Board()


def test_load_from_empty_sequence():
    assert Board.load([]).size() == (0, 0)


@mark.parametrize('data', [
    (['a']),
    (['ab']),
    (['a', 'b']),
])
def test_load(data):
    assert Board.load(data).size() == (len(data), max(map(len, data)))


@mark.parametrize('sequence, size', [
    ('', (0, 0)),
    ('a', (0, 0)),
    ('a', (1, 2)),
    ('ab', (3, 3)),
])
def test_random(sequence, size):
    board = Board.random(sequence, size)
    count = reduce(mul, size)
    letters = board.letters()
    assert board.size() == size and len(letters) == count and all(
        letter in sequence for letter in board.letters())
