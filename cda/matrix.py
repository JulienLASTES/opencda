# todo should do this in c
def norm_list(array: list) -> list:
    y = max([len(i) for i in array])
    for z in range(len(array)):
        while not len(array[z]) == y:
            array[z].append(0)
    return array


# a 2-dimensional list of elements only made of integers (+/-) [integer matrix]
class iMatrix:

    def __init__(self, x: int, y: int, array: list) -> None:
        self.x: int = int(x)
        self.y: int = int(y)
        self.array: list[list[int]] = array

    def __str__(self) -> str: return f'iMatrix ({self.x}x{self.y}).'
    def __getitem__(self, item: int) -> list[int]: return self.array[item]

    def __add__(self, other: ...) -> ...:
        if isinstance(other, iMatrix):
            if other.x == self.x and other.y == self.y:
                for x in range(self.x):
                    for y in range(self.y):
                        self[x][y] += other[x][y]
            else:
                # todo implement this case
                ...
            return self
        elif isinstance(other, int):
            for x in range(self.x):
                for y in range(self.y):
                    self[x][y] += other
            return self
        elif isinstance(other, float):
            # todo implement transformation to fpMatrix
            ...
        else:
            raise RuntimeError(f'"{self} + {other}": Unimplemented operand type.')

    @staticmethod
    def from_list(_list: list) -> ...:
        matrix = iMatrix(len(_list), max([len(x) for x in _list]), norm_list(_list))
        return matrix
