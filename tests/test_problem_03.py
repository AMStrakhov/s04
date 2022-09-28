from typing import Callable, Dict, List, Tuple

from problem_03 import count_letters
from .base_test_problem import BaseTestProblem


class TestProblem02(BaseTestProblem):
    _problem_func: Callable = count_letters
    cases: List[Tuple[List, Dict[str, int], str]] = [
        ([""], {}, "Empty String"),
        (["ABCABC"], {"a": 2, "b": 2, "c": 2}, "Upper-case"),
        (["abcabc"], {"a": 2, "b": 2, "c": 2}, "Lower-case"),
        (
            ["Red Apple"],
            {"r": 1, "e": 2, "d": 1, " ": 1, "a": 1, "p": 2, "l": 1},
            "Different letters and cases",
        ),
        (["  "], {" ": 2}, "Spaces"),
        (["\n\n\n"], {"\n": 3}, "Newlines"),
    ]

    def test_function(self) -> None:
        for inputs, expected, description in self.cases:
            with self.subTest(description):
                self.assertDictEqual(expected, self.problem_func(*inputs))
