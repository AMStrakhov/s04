from random import random
from time import perf_counter
from typing import Callable, List, Tuple

from problem_08 import execute
from .base_test_problem import BaseTestProblem


class TestProblem08(BaseTestProblem):
    _problem_func: Callable = execute
    cases: List[Tuple[List, str]] = [
        ([random, 5], "Random x5"),
        ([random, 0], "Random x0"),
        ([print, 5], "Print x5"),
    ]

    def test_function(self) -> None:
        for inputs, description in self.cases:
            with self.subTest(description):
                t1 = perf_counter()
                results, exec_time = self.problem_func(*inputs)
                t2 = perf_counter() - t1
                self.assertEqual(inputs[1], len(results))
                self.assertLessEqual(exec_time, t2)
                self.assertGreater(exec_time, 0)
