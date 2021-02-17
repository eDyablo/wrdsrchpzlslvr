from pytest import mark
from wrdpzl import (find_in_string, make_prefix_table)


@mark.parametrize('string, dictionary, words', [
    ('', [], []),
    ('a', ['a'], ['a']),
    ('ab', ['a', 'b'], ['a', 'b']),
    ('abcd', ['ab', 'cd'], ['ab', 'cd']),
    ('abxcd', ['ab', 'cd'], ['ab', 'cd']),
])
def test_words_from_dictionary_found_in_string(string, dictionary, words):
    assert find_in_string(string, dictionary) == words


@mark.parametrize('words, table', [
    ([], {}),
    (['a'], {'a': 'a'}),
    (['ab'], {'a': None, 'ab': 'ab'}),
])
def test_prefix_table_made_from_words(words, table):
    assert make_prefix_table(words) == table
