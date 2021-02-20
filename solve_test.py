from pytest import (fixture, mark)
from wrdpzl import(Board, solve)


@fixture
def words():
    return [
        'ad',
        'bag',
        'cage',
        'daily',
        'puzzle',
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
        'd.....',
        '.a....',
        '..i...',
        '...l..',
        '....y.',
    ]), ['daily']),
    (Board.load([
        '......',
        '......',
        'c.....',
        '.a....',
        '..g...',
        '...e..',
    ]), ['cage']),
    (Board.load([
        '......',
        '......',
        '......',
        'b.....',
        '.a....',
        '..g...',
    ]), ['bag']),
    (Board.load([
        '......',
        '......',
        '......',
        '......',
        'a.....',
        '.d....',
    ]), ['ad']),
    (Board.load([
        '.d....',
        '..a...',
        '...i..',
        '....l.',
        '.....y',
        '......',
    ]), ['daily']),
    (Board.load([
        '..c...',
        '...a..',
        '....g.',
        '.....e',
        '......',
        '......',
    ]), ['cage']),
    (Board.load([
        '...b..',
        '....a.',
        '.....g',
        '......',
        '......',
        '......',
    ]), ['bag']),
    (Board.load([
        '....a.',
        '.....d',
        '......',
        '......',
        '......',
        '......',
    ]), ['ad']),
])
def test_find_words_on(board, words, expected):
    assert solve(board, words) == expected
