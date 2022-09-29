from typing import Callable, List, Tuple

from problem_04 import sort_words
from .base_test_problem import BaseTestProblem


class TestProblem04(BaseTestProblem):
    _problem_func: Callable = sort_words
    cases: List[Tuple[List[str], str, str]] = [
        (["red-yellow-black-blue"], "black-blue-red-yellow", "Base Case"),
        (["red"], "red", "One Word"),
        ([""], "", "Empty String"),
        (
            ["красный-жёлтый-чёрный-синий"],
            "жёлтый-красный-синий-чёрный",
            "Cyrillic",
        ),
    ]

    def test_function(self) -> None:
        self._test_function()
