"""
Description:

Write a function that accepts any number of positional and key arguments and
returns a string. The string should have the following format:
"<1st argument index or key>: <1st argument value>;
<2nd argument index or key>: <2nd argument value>;
...
<n-th argument index or key>: <n-th argument value>."

Positional arguments should come first, and key arguments — after them.

If no arguments were passed, return None.

Examples:
arguments: 2022, "hse", arr=[0, 1], json={"iso": "RU"}
result: "0: 2022; 1: hse; arr: [0, 1]; json: {'iso': 'RU'}."
"""
from typing import Optional


def collect_arguments(...) -> Optional[str]:
    """Write your solution here:"""
    ...


if __name__ == "__main__":
    print(collect_arguments(2022, "hse", arr=[0, 1], json={"iso": "RU"}))
