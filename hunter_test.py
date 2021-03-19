from pytest import mark
from wrdpzl import Hunter

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
    assert hunter.find(string) == words
