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


def test_three_diagonal_cells_inserted_into(empty_grid):
    grid = empty_grid
    for i in range(2, -1, -1):
        grid[i, i] = i
    assert grid.cell_count() == 3
    assert grid.size() == (3, 3)
    for i in range(0, 3):
        assert grid[i, i] == i
