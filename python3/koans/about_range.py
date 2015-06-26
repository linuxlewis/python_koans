from runner.koan import *
import functools
import collections.abc


class AboutRange(Koan):
    """
    range(stop)
    range(start, stop[, step]) is a builtin function that returns an range object from start to stop by step.
    """

    def test_range_is_a_sequence(self):

        self.assertEqual(__, isinstance(range(1), collections.abc.Sequence))

    def test_range_is_not_an_iterator(self):

        with self.assertRaises(__):
            next(range(1))  # should raise a TypeError

        self.assertRaises(__, test)

    def test_range_can_be_an_iterator(self):

        iter_range = iter(range(1))

        self.assertEqual(__, next(iter_range))

    def test_range_can_iterate(self):
        result = []
        for x in range(3):
            result.append(x)
        self.assertEqual(__, result)

    def test_range_can_have_a_length(self):

        self.assertEqual(__, len(range(5)))

    def test_range_starts_with_zero_by_default(self):

        self.assertEqual(__, range(1).start)

    def test_range_can_return_value_at_index(self):

        self.assertEqual(__, range(10).index(5))

    def test_range_can_start_at_another_value(self):

        result = []
        for x in range(1, 4):
            result.append(x)

        self.assertEqual(__, result)

    def test_range_can_step_by_value(self):

        result = []
        for x in range(0, 50, 5):
            result.append(x)

        self.assertEqual(__, result)

    def test_range_can_go_negative(self):

        result = []
        for x in range(0, -5, -1):
            result.append(x)

        self.assertEqual(__, result)

    def test_range_with_map(self):

        result = list(map(lambda x: x * 2, range(5)))

        self.assertEqual(__, result)

    def test_range_can_work_with_other_iterators(self):

        def factorial(n):
            return functools.reduce(lambda x, total: x * total, range(1, n + 1))

        self.assertEqual(__, factorial(2))  # 2!
