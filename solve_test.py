from pytest import (fixture, mark)
from wrdpzl import(Board, solve)


@fixture
def words():
    return [
        'acmes',
        'babe',
        'cab',
        'puzzle',
        'puzzled',
        'puzzlement',
        'puzzler',
        'puzzlers',
        'puzzles',
        'puzzling',
    ]


@mark.parametrize('board, expected', [
    (Board.load([
        'puzzle',
    ]), ['puzzle']),
    (Board.load([
        '',
        'puzzle',
    ]), ['puzzle']),
    (Board.load([
        '',
        '',
        'puzzle',
    ]), ['puzzle']),
    (Board.load([
        'p__',
        'u__',
        'z__',
        'z__',
        'l__',
        'e__',
    ]), ['puzzle']),
    (Board.load([
        '__p',
        '__u',
        '__z',
        '__z',
        '__l',
        '__e',
    ]), ['puzzle']),
    (Board.load([
        'p.....',
        '.u....',
        '..z...',
        '...z..',
        '....l.',
        '.....e',
    ]), ['puzzle']),
    (Board.load([
        '......',
        'a.....',
        '.c....',
        '..m...',
        '...e..',
        '....s.',
    ]), ['acmes']),
    (Board.load([
        '......',
        '......',
        'b.....',
        '.a....',
        '..b...',
        '...e..',
    ]), ['babe']),
    (Board.load([
        '......',
        '......',
        '......',
        'c.....',
        '.a....',
        '..b...',
    ]), ['cab']),
])
def test_find_words_on(board, words, expected):
    assert solve(board, words) == expected
