from pytest import (fixture, mark)
from wrdpzl import(Board, Solver)


@fixture(scope='module')
def words():
    with open('words.txt') as file:
        return list(map(str.strip, file.readlines()))


@fixture(scope='module')
def solver(words):
    return Solver(words)


@mark.timeout(0.5)
@mark.parametrize('board', [
    (Board.load(['performance'] * 10)),
    (Board.load(['top' * 5] * 15)),
    (Board.load(['up' * 75] * 150)),
])
def test_performance(board, solver):
    assert solver.solve(board) != []
