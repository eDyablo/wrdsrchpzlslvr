class Grid:
    def __init__(self):
        self.__cells = dict()

    def cell_count(self):
        return len(self.__cells)

    def size(self):
        return self.__row_count, self.__column_count

    def __setitem__(self, key, value):
        row, column = key
        index = self.__index(row, column)
        self.__cells[index] = value
        self.__row_count, self.__column_count = row + 1, column + 1

    def __getitem__(self, key):
        index = self.__index(*key)
        return self.__cells[index]

    def __index(self, row, column):
        return f'{row}x{column}'
