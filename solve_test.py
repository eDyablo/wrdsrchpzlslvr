from pytest import (fixture, mark)
from wrdpzl import(Board, solve)


@fixture
def words():
    return [
        'at',
        'box',
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
        '.o....',
        '..x...',
    ]), ['box']),
    (Board.load([
        '......',
        '......',
        '......',
        '......',
        'a.....',
        '.t....',
    ]), ['at']),
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
        '....o.',
        '.....x',
        '......',
        '......',
        '......',
    ]), ['box']),
    (Board.load([
        '....a.',
        '.....t',
        '......',
        '......',
        '......',
        '......',
    ]), ['at']),
    (Board.load([
        '.txeye',
        'aogll.',
        'baiz..',
        'caz...',
        'du....',
        'p.....',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        '.....e',
        '....ly',
        '...zle',
        '..zigx',
        '.uaaot',
        'pdcba.',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
])
def test_find_words_on(board, words, expected):
    assert sorted(solve(board, words)) == expected
