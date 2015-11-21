class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
    """Iter"""
    def __iter__(self):
        return self
    """Next"""
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()