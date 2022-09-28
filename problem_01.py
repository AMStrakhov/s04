"""
Description:

Write a function that accepts a list of strings.
It should return a dict, in which the keys are strings' lengths
and the values are their counts.
Don't count types that are not strings.


Examples:
arguments: ['abc', 'ab', 'asd', '1221']
result: {2: 1, 3: 2, 4: 1}

arguments: ['abc', 1, 'asd', [1, 2]]
result: {3: 2}

"""
from typing import Dict, List


def count_strings_lengths(strings: List[str]) -> Dict[int, int]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(count_strings_lengths(["abc", "ab", "asd", "1221"]))
