from pytest import fixture
from wrdpzl import find_in_string


@fixture
def empty_string():
    return ''


@fixture
def empty_dictionary():
    return []


def test_no_words_found_in(empty_string, empty_dictionary):
    found = find_in_string(empty_string, empty_dictionary)
    assert len(found) == 0


def test_one_letter_word_found_in_string_containing_only_the_word():
    found = find_in_string('a', ['a'])
    assert len(found) == 1 and 'a' in found
