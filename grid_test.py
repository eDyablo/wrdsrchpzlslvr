from grid import Grid
from pytest import fixture


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


def test_iteration_along_each_row_of_the(filled_grid):
    row_count, column_count = filled_grid.size()
    for row in range(0, row_count):
        assert list(filled_grid.iterate((row, 0), (0, 1))) == [
            (row, column) for column in range(0, column_count)]


def test_iteration_along_each_column_of_the(filled_grid):
    row_count, column_count = filled_grid.size()
    for column in range(0, column_count):
        assert list(filled_grid.iterate((0, column), (1, 0))) == [
            (row, column) for row in range(0, row_count)]
