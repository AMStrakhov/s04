from typing import Callable, List, Tuple

from problem_05 import replace_last_element
from .base_test_problem import BaseTestProblem


class TestProblem05(BaseTestProblem):
    _problem_func: Callable = replace_last_element
    cases: List[Tuple[List, List[Tuple], str]] = [
        (
            [[(1, 2, 3), (3, 2, 1), (1, 2)], 100],
            [(1, 2, 100), (3, 2, 100), (1, 100)],
            "Base Case",
        ),
        ([[], 100], [], "Empty List"),
        (
            [[(1, 2, 3), (3, 2, 1), ()], 100],
            [(1, 2, 100), (3, 2, 100), ()],
            "Empty Tuple",
        ),
        (
            [[(1, 2, 3), (3, 2, 1), (1, 2)], None],
            [(1, 2, None), (3, 2, None), (1, None)],
            "Replace with None",
        ),
        (
            [[(1, 2, 3), (3, 2, 1), (1, 2)], "x"],
            [(1, 2, "x"), (3, 2, "x"), (1, "x")],
            "Replace with String",
        ),
    ]

    def test_function(self) -> None:
        for args, expected, description in self.cases:
            with self.subTest(description):
                self.assertListEqual(expected, self.problem_func(*args))
