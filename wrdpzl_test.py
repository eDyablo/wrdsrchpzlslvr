from pytest import (fixture, mark)
from wrdpzl import (Board, Hunter, make_prefix_table, solve)

alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']


@mark.parametrize('string, dictionary, words', [
    ('', [], []),
    ('a', ['a'], ['a']),
    ('ab', ['a', 'b'], ['a', 'b']),
    ('a', ['a', 'ab'], ['a']),
    ('abcd', ['ab', 'cd'], ['ab', 'cd']),
    ('abxcd', ['ab', 'cd'], ['ab', 'cd']),
    ('abc', ['ab', 'bc'], ['ab', 'bc']),
    ('abc', ['abc', 'bc'], ['abc', 'bc']),
    ('abcd', ['abcd', 'bc'], ['bc', 'abcd']),
    (''.join(alphabet), alphabet, alphabet),
    (''.join(alphabet), [''.join(alphabet)], [''.join(alphabet)]),
    ('start', ['start', 'star', 'art', 'tart'],
     ['star', 'start', 'tart', 'art']),
    ('aacarelessaa', ['careless', 'care', 'car', 'less', 'are'], [
     'car', 'care', 'are', 'careless', 'less']),
    ('scosmo', ['cosmos'], []),
])
def test_words_from_dictionary_found_in_string(string, dictionary, words):
    hunter = Hunter(dictionary)
    assert hunter.find_in_string(string) == words


@mark.parametrize('words, table', [
    ([], {}),
    (['a'], {'a': 'a'}),
    (['ab'], {'a': None, 'ab': 'ab'}),
    (['a', 'ab'], {'a': 'a', 'ab': 'ab'}),
])
def test_prefix_table_made_from_words(words, table):
    assert make_prefix_table(words) == table


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


@fixture
def words():
    return [
        'puzzle',
        'puzzled',
        'puzzlement',
        'puzzler',
        'puzzlers',
        'puzzles',
        'puzzling',
    ]


@mark.parametrize('board', [
    (Board.load([
        'puzzle',
    ])),
    (Board.load([
        '',
        'puzzle',
    ])),
    (Board.load([
        '',
        '',
        'puzzle',
    ])),
    (Board.load([
        'p__',
        'u__',
        'z__',
        'z__',
        'l__',
        'e__',
    ])),
    (Board.load([
        '__p',
        '__u',
        '__z',
        '__z',
        '__l',
        '__e',
    ]))
])
def test_find_words_in_rows(board, words):
    assert solve(board, words) == ['puzzle']
