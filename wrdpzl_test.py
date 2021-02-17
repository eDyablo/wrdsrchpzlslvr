from pytest import fixture
from wrdpzl import find_in_string


@fixture
def empty_string():
    return ''


def test_no_words_found_in(empty_string):
    found = find_in_string('')
    assert len(found) == 0
