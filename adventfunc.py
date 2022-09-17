from collections import defaultdict, namedtuple

# A lot of puzzles work around a board or a matrix of values.

Point = namedtuple('Point', ['x', 'y'])

class SparseBoard():
    """Sparse Board as a dict of dict. First dictionary represents all used x-coords and for any existing x-coord will return a dict of associated y-coord.
    If the board is wider or taller than any of the given x,y coordinates, you can define a width and a height. 
    All points durint board creation must be inside the defined width and height.
    If width or height is None, that dimenstion will be defined by the points given during init.
    After creation, no points can be added outside the board.
    
    """
    def __init__(
            self,
            points: list = None,
            value_held = True, 
            width: int|None = None, 
            height: int|None = None
    ):
        self.xy = defaultdict(lambda: defaultdict(lambda: None))

        cur_width  = 0
        cur_height = 0

        if value_held is None:
            raise ValueError("`value_held` cannot be `None`.")
        else:
            for (x, y) in points:
                width = max(cur_width, x+1)
                height = max(cur_height, y+1)
                self.xy[x][y] = value_held

        if width:
            if (width < 0) or (int(width) != width):
                raise ValueError(f"Width must be a positive integer. Received {width=}")
            if width < cur_width:
                raise ValueError("There are points outside the defined width")
            self.width = width
        else:
            self.width = cur_width
        
        if height:
            if (height < 0) or (int(height) != height):
                raise ValueError(f"Height must be a positive integer. Received {height=}")
            if height < cur_height:
                raise ValueError("There are points outside the defined height")
        else:
            self.height = cur_height
        
        self.shape = (self.width, self.height)

    def __getitem__(self, key):
        x, y = key

        errors = []
        if x >= self.width:
            errors.append(IndexError(f"x-index is outside of board. Expected x to be <= to board height of {self.height}, but received {x}"))
        if y >= self.height:
            errors.append(IndexError(f"y-index is outside of board. Expected y to be <= to board width of {self.width}, but received {y}"))
        if errors:
            raise Exception(errors)

        return self.xy[x][y]
    
    def __repr__(self) -> str:
        def draw_board():
            for y in range(self.height):
                for x in range(self.width):
                    yield "*" if self[x,y] else "."
                yield '\n'
        
        return "".join(draw_board())


class SparseBoard(list):
    """SparseBoard as a list of points"""
    def __init__(self, items):
        xs, ys = [],[]
        for (x, y) in items:
            xs.append(x)
            ys.append(y)
        
        self.width = max(xs) + 1
        self.height = max(ys) + 1

        self.shape = (self.width, self.height)

        super().__init__(items)

    def __getitem__(self, key):

        for point in self.__iter__():
            if key == point:
                return True
        else:
            return False

class SparseBoard(set):
    """SparseBoard as a set of points"""
    def __init__(self, items):
        xs, ys = [],[]
        for (x, y) in items:
            xs.append(x)
            ys.append(y)
        
        self.width = max(xs) + 1
        self.height = max(ys) + 1

        self.shape = (self.width, self.height)

        super().__init__(items)

    def __getitem__(self, key):
        return key in self

    def __setitem__(self, key, value):
        if self[key]:
            self.remove(key)
        self.add(value)

    @property
    def xs(self):
        return [x for x,y in self]

    @property
    def ys(self):
        return [y for x,y in self]
