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
