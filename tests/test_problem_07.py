from typing import Callable, List, Set, Tuple

from problem_07 import find_common
from .base_test_problem import BaseTestProblem


class TestProblem07(BaseTestProblem):
    _problem_func: Callable = find_common
    cases: List[Tuple[List, Set, str]] = [
        ([[], []], set(), "Empty lists"),
        ([["a", "b", "a", "b", "b"], ["a"]], {"a"}, "Chars"),
        (
            [["abc abc", "abc", "abc"], ["abc abc", "xyz"]],
            {"abc abc"},
            "Strings",
        ),
        ([[2, 2, 1, 0, 1, 1, 2, 3], [2, 0, 4]], {2, 0}, "Integers"),
        ([[2, 2, "a", 1, 0, 1, 1, 2], [2, 0, "a", "z"]], {2, "a", 0}, "Mixed"),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                result = self.problem_func(*inputs)
                self.assertEqual(len(expected), len(result))
                self.assertSetEqual(expected, set(result))
