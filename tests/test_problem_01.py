from typing import Callable, Dict, List, Tuple

from problem_01 import count_strings_lengths
from .base_test_problem import BaseTestProblem


class TestProblem08(BaseTestProblem):
    _problem_func: Callable = count_strings_lengths
    cases: List[Tuple[List, Dict[int, int], str]] = [
        ([[]], {}, "Empty list"),
        ([["a", "b", "a", "ab", ""]], {0: 1, 1: 3, 2: 1}, "Base Case"),
        (
            [["a", [1, 2], "a", 0, "", {"a": "b"}]],
            {0: 1, 1: 2},
            "Different Types",
        ),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                self.assertDictEqual(expected, self.problem_func(*inputs))
