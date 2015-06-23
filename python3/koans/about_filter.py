from runner.koan import *


class AboutFilter(Koan):
    """
    filter(lambda, iterable) is a builtin method that returns an iterator that contains only
    the elements for which lambda(x) == True
    """

    def test_filter_returns_iterator(self):
        """
        An iterator is an object that can be iterated over (with a loop)
        """
        stay_positive = lambda x: x > 0

        result = []
        for x in filter(stay_positive, [-1, 0, 1]):
            result.append(x)

        self.assertEqual(__, result)

    def test_filter_with_function(self):
        """
        The filter function should filter items based on the function passed to it
        """
        less_than_zero = lambda x: x < 0
        test_list = [-3, -1, 0, 5]
        self.assertEqual(__, list(filter(less_than_zero, test_list)))

    def test_filter_with_callable(self):
        """
        The filter function can take any callable that returns a boolean
        """
        test_list = [1, 2, 3, 4]
        self.assertEqual(__, list(filter(self._filter_stuff, test_list)))

    def _filter_stuff(self, x):
        return x % 2 == 0

    def test_filter_none_function(self):
        """
         If function is None, the identity function is assumed.
         That is, all elements of iterable that are false are removed.
         ie. list.remove(x) if not x
        """
        self.assertEqual(__, list(filter(None, [True, False, True, False])))

    def test_filter_without_filter(self):
        """
        The filter function is just shorthand for a list comprehension
        """
        greater_then_zero = lambda x: x > 0
        test_list = [-2, -1, 0, 1, 2]
        self.assertEqual(__, [item for item in test_list if greater_then_zero(item)])
