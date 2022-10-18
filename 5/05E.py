from __future__ import annotations
from typing import Union, Iterable, List
import random
import itertools

def flatten(l):
    return [item for sublist in l for item in sublist]

class CardStack:
    values: List[int]

    def __init__(self, val: Union[int, Iterable[int], None] = None):
        self.values = list()
        if isinstance(val, int):
            sst = list([random.randint(-100, 100) for x in range(val)])
            self.values = sst
            # random.sample(range(-100, 101), val)
        if isinstance(val, Iterable) and all(isinstance(n, int) for n in val):
            self.values = list(val)
        """If val is None values is an empty list
         If val is int fills values with val random integers between -100 and 100
         If val is Iterable[int] fills values from val
        """

    def shuffled(self) -> CardStack:
        """Returns a new CardStack instance with shuffled values"""
        values = self.values.copy()
        random.shuffle(values)
        random.shuffle(values)
        random.shuffle(values)

        return CardStack(values)

    def combine(self, other: CardStack) -> CardStack:
        """Returns a new CardStack instance with self and other values combined one after another
         [1, 2, 3], [4, 5, 6, 7] -> [1, 4, 2, 5, 3, 6, 7]
            """
        result = [x for x in flatten([x for x in itertools.zip_longest(self.values, other.values)]) if x is not None]
        return CardStack(result)

    def add(self, value: int) -> None:
        """Adds a new value on top of the stack"""
        self.values.append(value)

    def __len__(self) -> int:
        """Returns the size of the stack"""
        return len(self.values)

num = CardStack(5)
num.add(2)
one = CardStack([1, 2, 3])
two = CardStack([4, 5, 6, 7])
print(one.combine(two).values)
stackT = CardStack(tuple([12, 21, 34, 53]))
stackArr = CardStack([6, 3, 5, 64,2342,34,1,3,4,35,43,6,35,])
print(stackArr.values)
stackArr.add(222)
print(stackArr.combine(stackT).values)
stackNone = CardStack(None)
print(stackT.values)
print(stackArr.values)
print(stackNone.values)
stackT.add(1)
print(stackT.values)
combined = stackNone.combine(stackArr)
print(combined.values)
stackNone.add(2)
print(stackNone.values)
print(combined.values)
print(len(combined))
shuffled = combined.shuffled()
print(shuffled.values)
print(len(shuffled))
print(combined.values)
srt = CardStack(2000)
print(min(srt.values))
print(max(srt.values))
