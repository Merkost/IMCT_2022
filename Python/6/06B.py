from __future__ import annotations
import itertools
import sys
from collections.abc import Generator, Iterable


def take(iterable: Iterable, *, skip: int = 0, step: int = 1, count: int | None = None) -> Generator:
    '''
    Yields every `step`-th value from `iterable` skipping first `skip` values.
    If `count` is not None yields this many values at most.

    Args:
        iterable: Iterable to take values from
        skip: Number of values to skip from the beginning, non-negative integer
        step: Skip `step` - 1 values between every yield, positive integer
        count: Yields this many values at most, None or non-negative integer

    Raises:
        ValueError:
            `skip` or `count` is less than 0
            `step` is less than 1
        TypeError:
            `skip`, `step` is not an int or `iterable` is not an Iterable
            `count` is not an int or None

    '''
    if skip < 0 or (count is not None and count < 0) or step < 1:
        raise ValueError
    if not isinstance(iterable, Iterable) or not isinstance(step, int) or not isinstance(skip, int):
        raise TypeError
    if not isinstance(count, int) and count is not None:
        raise TypeError

    myIter = itertools.islice(iterable, skip, sys.maxsize, step)

    if (count is not None):
        return (v for v in itertools.islice(myIter, count))
    else:
        return (v for v in myIter)

print(*take(range(100), skip=5, step=5, count = 5))
