from pytest import mark
from wrdpzl import make_prefix_table


@mark.parametrize('words, table', [
    ([], {}),
    (['a'], {'a': 'a'}),
    (['ab'], {'a': None, 'ab': 'ab'}),
    (['a', 'ab'], {'a': 'a', 'ab': 'ab'}),
])
def test_prefix_table_made_from_words(words, table):
    assert make_prefix_table(words) == table
