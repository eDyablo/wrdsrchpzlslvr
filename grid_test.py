from pytest import fixture
from grid import Grid


@fixture
def grid():
    return Grid()


def test_empty(grid):
    assert grid.cell_count() == 0
    assert grid.size() == (0, 0)


def test_one_cell_when_insert_into_0_0_cell_of(grid):
    grid[0, 0] = 1
    assert grid.cell_count() == 1
    assert grid[0, 0] == 1
    assert grid.size() == (1, 1)


def test_three_diagonal_cells_inserted_into(grid):
    for i in range(2, -1, -1):
        grid[i, i] = i
    assert grid.cell_count() == 3
    assert grid.size() == (3, 3)
    for i in range(0, 3):
        assert grid[i, i] == i


def test_no_cells_in_empty(grid):
    for r in range(0, 9):
        for c in range(0, 9):
            assert grid[r, c] == None
    assert grid.size() == (0, 0)
    assert grid.cell_count() == 0


def test_the_containment_operator_of(grid):
    grid[1, 1] = 1
    assert (0, 0) not in grid
    assert (0, 1) not in grid
    assert (0, 2) not in grid
    assert (1, 0) not in grid
    assert (2, 0) not in grid
    assert (1, 1) in grid
    assert (1, 2) not in grid
    assert (2, 1) not in grid
    assert (2, 2) not in grid


@fixture
def filled_grid(grid):
    for row in range(0, 5):
        for column in range(0, 5):
            grid[row, column] = (row, column)
    return grid


def test_content_of(filled_grid):
    rows, columns = filled_grid.size()
    for row in range(0, rows):
        for column in range(0, columns):
            assert filled_grid[row, column] == (row, column)
