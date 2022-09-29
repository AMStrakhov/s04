"""
Description:
Write a function that executes another function n times and counts
total execution time (time.perf_counter).
It should return a tuple, where the first element is a list of execution
results, and the second is a total execution time (n times).


Examples:
arguments: random, 5
result: [0.1, 0.2, 0.3, 0.4, 0.5], 0.00123
"""
from random import random
from time import perf_counter
from typing import Callable, List, Tuple


def execute(func: Callable, n: int) -> Tuple[List, float]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(execute(random, 5))
