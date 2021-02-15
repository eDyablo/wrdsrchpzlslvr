class Grid:
    def __init__(self):
        self.__cells = dict()
        self.__size = 0, 0

    def cell_count(self):
        return len(self.__cells)

    def size(self):
        return self.__size

    def __setitem__(self, key, value):
        row, column = key
        index = self.__index(row, column)
        self.__cells[index] = value
        self.__size = max(self.__size[0], row +
                          1), max(self.__size[1], column + 1)

    def __getitem__(self, key):
        index = self.__index(*key)
        return self.__cells[index] if index in self.__cells else None

    def __index(self, row, column):
        return f'{row}x{column}'

    def __contains__(self, key):
        return self.__index(*key) in self.__cells
