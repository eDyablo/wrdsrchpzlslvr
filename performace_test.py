from pytest import (fixture, mark)
from wrdpzl import(Board, solve)


@fixture(scope='module')
def words():
    with open('words.txt') as file:
        return list(map(str.strip, file.readlines()))


@mark.timeout(0.5)
@mark.parametrize('board', [
    (Board.load(['top' * 5] * 15)),
    (Board.load(['up' * 50] * 100)),
])
def test_performance(board, words):
    assert solve(board, words) != []
