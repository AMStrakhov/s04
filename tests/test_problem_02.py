from typing import Callable, List, Set, Tuple

from problem_02 import remove_duplicates
from .base_test_problem import BaseTestProblem


class TestProblem02(BaseTestProblem):
    _problem_func: Callable = remove_duplicates
    cases: List[Tuple[List, Set, str]] = [
        ([[]], set(), "Empty list"),
        ([["a", "b", "a", "b", "b"]], {"a", "b"}, "Chars"),
        ([["abc abc", "abc", "abc"]], {"abc abc", "abc"}, "Strings"),
        ([[2, 2, 1, 0, 1, 1, 2]], {2, 1, 0}, "Integers"),
        ([[2, 2, "a", 1, 0, 1, 1, 2]], {2, "a", 1, 0}, "Mixed"),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                result = self.problem_func(*inputs)
                self.assertEqual(len(expected), len(result))
                self.assertSetEqual(expected, set(result))
