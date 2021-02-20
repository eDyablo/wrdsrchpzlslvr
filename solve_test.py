from pytest import (fixture, mark)
from wrdpzl import(Board, solve)


@mark.parametrize('board, words', [
    (Board.load([
        'at',
        'box',
        'cage',
        'daily',
        'puzzle',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        'abcdp',
        'toaau',
        '.xgiz',
        '..elz',
        '...yl',
        '....e',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        'p.....',
        'du....',
        'caz...',
        'baiz..',
        'aogll.',
        '.txeye',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        'pdcba.',
        '.uaaot',
        '..zigx',
        '...zle',
        '....ly',
        '.....e',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
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
    (Board.load([
        'elzzup',
        'yliad',
        'egac',
        'xob',
        'ta',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        '    e',
        '   yl',
        '  elz',
        ' xgiz',
        'toaau',
        'abcdp',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        'e',
        'yl',
        'elz',
        'xgiz',
        'toaau',
        ' abcdp',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        'eyext',
        ' llgoa',
        '  ziab',
        '   zac',
        '    ud',
        '     p',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        ' abcdp',
        'toaau',
        'xgiz',
        'elz',
        'yl',
        'e',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
    (Board.load([
        '     p',
        '    ud',
        '   zac',
        '  ziab',
        ' llgoa',
        'eyext',
    ]), ['at', 'box', 'cage', 'daily', 'puzzle']),
])
def test_solve(board, words):
    assert sorted(solve(board, words)) == words
