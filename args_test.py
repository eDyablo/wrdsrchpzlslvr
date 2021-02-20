from pytest import mark
from wrdpzl import parse_size


@mark.parametrize('text, size', [
    ('', (0, 0)),
    (' ', (0, 0)),
    ('1', (1, 1)), ('2 ', (2, 2)), (' 3 ', (3, 3)),
    ('1 2', (1, 2)), ('2,3', (2, 3)), ('3x4', (3, 4)), ('40*50', (40, 50)),
    (' 1 2 ', (1, 2)), (' 2 , 3 ', (2, 3)),
    (' 3 x 4 ', (3, 4)), (' 40 * 50 ', (40, 50)),
])
def test_parse_size(text, size):
    assert parse_size(text) == size
