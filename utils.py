import multiprocessing
import multiprocessing.pool
from typing import Tuple, Any
import unittest
import pickle
import functools


def load_test_case() -> Tuple[Any, Any, Any]:
    with open('test_data_partial.bin', 'rb') as f:
        return pickle.load(f)


def timeout(max_timeout):
    def timeout_decorator(item):
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            try:
                res = async_result.get(max_timeout)
            except multiprocessing.context.TimeoutError:
                res = None
            finally:
                pool.close()
            return res
        return func_wrapper
    return timeout_decorator


class TestP1(unittest.TestCase):
    def setUp(self) -> None:
        q1a_test_cases, q1b_test_cases, q1c_test_cases = load_test_case()
        self.q1a_test_cases = q1a_test_cases
        self.q1b_test_cases = q1b_test_cases
        self.q1c_test_cases = q1c_test_cases

    def testQ1a(self):
        from A3_P1_1a import mazeQ1a

        for test_case in self.q1a_test_cases:
            graph, start, end, time = test_case
            with self.subTest():
                self.assertEqual(mazeQ1a(graph, start, end), time)

    def testQ1b(self):
        from A3_P1_1b import mazeQ1b

        for test_case in self.q1b_test_cases:
            graph, start, end, F, time = test_case
            with self.subTest():
                self.assertEqual(mazeQ1b(graph, start, end, F), time)

    def testQ1c(self):
        from A3_P1_1c import mazeQ1c

        for test_case in self.q1c_test_cases:
            graph, start, end, F, time = test_case
            with self.subTest():
                self.assertEqual(mazeQ1c(graph, start, end, F), time)


if __name__ == '__main__':
    unittest.main()
