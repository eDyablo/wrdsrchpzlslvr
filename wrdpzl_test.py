from pytest import mark
from wrdpzl import find_in_string


@mark.parametrize('string, dictionary, words', [
    ('', [], []),
    ('a', ['a'], ['a']),
])
def test_words_from_dictionary_found_in_string(string, dictionary, words):
    assert find_in_string(string, dictionary) == words
