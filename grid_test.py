from pytest import fixture
from grid import Grid


@fixture
def empty_grid():
    return Grid()


def test_no_cells_in(empty_grid):
    assert empty_grid.cell_count() == 0

def test_one_cell_when_insert_into_0_0_cell_of(empty_grid):
    grid = empty_grid
    grid[0, 0] = 1
    assert grid.cell_count() == 1
    assert grid[0, 0] == 1
    assert grid.size() == (1, 1)
