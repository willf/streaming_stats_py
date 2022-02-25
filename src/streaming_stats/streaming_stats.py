import math

__version__ = "0.1.0"

class StreamingStats:
    def __init__(self, epsilon=0.1):
        self.epsilon = epsilon
        self.one_over_2e = 1 / (2 * epsilon)
        self.n = 0
        self.mean = 0.0
        self.M2 = 0.0
        self.min = None
        self.max = None
        self.sum = 0.0
        self.S = []

    def update(self, i):
        self.n += 1
        self.sum += i
        self.delta = i -self.mean
        self.mean += (self.delta / self.n)
        self.M2 += self.delta * (i - self.mean)
        if self.min is None or self.max is None:
            self.min = i
            self.max = i
        else:
            self.min = min(self.min, i)
            self.max = max(self.max, i)

    def append(self, i):
        self.update(i)

    def __len__(self):
        return self.n

    def extend(self, iterable):
        for i in iterable:
            self.append(i)

    def mean(self):
        return self.mean

    def variance(self):
        if self.n <= 1:
            return 0.0
        return self.M2 / (self.n)

    def stddev(self):
        return math.sqrt(self.variance())

    def max(self):
        return self.max

    def min(self):
        return self.min

    def sum(self):
        return self.sum

    def dict(self):
        return {
            "n": self.n,
            "mean": self.mean,
            "variance": self.variance(),
            "stddev": self.stddev(),
            "min": self.min,
            "max": self.max,
            "sum": self.sum,
        }


def stats(iterable, accumulator=StreamingStats()):
    accumulator.extend(iterable)
    return accumulator.dict()
