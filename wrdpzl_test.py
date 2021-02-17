from pytest import mark
from wrdpzl import (find_in_string, make_prefix_table)

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
    assert find_in_string(string, dictionary) == words


@mark.parametrize('words, table', [
    ([], {}),
    (['a'], {'a': 'a'}),
    (['ab'], {'a': None, 'ab': 'ab'}),
    (['a', 'ab'], {'a': 'a', 'ab': 'ab'}),
])
def test_prefix_table_made_from_words(words, table):
    assert make_prefix_table(words) == table
