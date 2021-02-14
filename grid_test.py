from pytest import fixture
from grid import Grid


@fixture
def empty_grid():
    return Grid()


def test_no_cells_in(empty_grid):
    assert empty_grid.cell_count() == 0
