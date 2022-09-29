"""
Description:

Write a function that replaces the last element of each tuple in a list
with the second argument's value.
If a tuple is empty, leave it without a replacement.

Examples:
arguments: [(1, 2, 3), (3, 2, 1), (1, 2)], 100
result: [(1, 2, 100), (3, 2, 100), (1, 100)]

arguments: [(1, 2, 3), (3, 2, 1), ()], "abc"
result: [(1, 2, "abc"), (3, 2, "abc"), ()]
"""
from typing import Any, List, Tuple


def replace_last_element(sequence: List[Tuple], new_value: Any) -> List[Tuple]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(replace_last_element([(1, 2, 3), (3, 2, 1), (1, 2)], new_value=100))
