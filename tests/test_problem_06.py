from typing import Callable, Dict, List, Tuple

from problem_06 import collect_arguments
from .base_test_problem import BaseTestProblem


class TestProblem06(BaseTestProblem):
    _problem_func: Callable = collect_arguments
    cases: List[Tuple[List, Dict, Dict[str, int], str]] = [
        (
            [2022, "hse"],
            dict(arr=[0, 1], json={"iso": "RU"}),
            "0: 2022; 1: hse; arr: [0, 1]; json: {'iso': 'RU'}.",
            "Base Case",
        ),
        (
            [2022, "hse"],
            {},
            "0: 2022; 1: hse.",
            "Only Args",
        ),
        (
            [],
            dict(arr=[0, 1], json={"iso": "RU"}),
            "arr: [0, 1]; json: {'iso': 'RU'}.",
            "Only Kwargs",
        ),
        ([], {}, None, "No Args/Kwargs"),
    ]

    def test_function(self) -> None:
        for args, kwargs, expected, description in self.cases:
            with self.subTest(description):
                self.assertEqual(expected, self.problem_func(*args, **kwargs))
