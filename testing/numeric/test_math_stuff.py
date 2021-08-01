import unittest
from math_stuff import calc_avg_two_numbers
from math_stuff import calc_roi_one_period
from math_stuff import calc_pythagorean_theorem_side
from math_stuff import calc_pythagorean_theorem_hyp


# note - I had to create in pwd file "__init__.py" before tests could execute
class math_stuff_TestCase(unittest.TestCase):
    """Tests for math_stuff.py.
    Never update your test to make things work. Update your code!"""

    # "test_"function_name
    def test_calc_avg_two_numbers(self):
        """Tests for the average function."""

        # assert equal
        result = calc_avg_two_numbers(10, 10)
        self.assertEqual(result, 10)

        result = calc_avg_two_numbers(-10, 10)
        self.assertEqual(result, 0)

        # assert true
        result = calc_avg_two_numbers(6, 1)
        self.assertTrue(isinstance(result, float))

        # greater than
        result = calc_avg_two_numbers(6, 1)
        self.assertGreaterEqual(6 + 1, result)

    def test_calc_roi_one_period(self):
        """Tests for the return on investment function."""

        result = calc_roi_one_period(5, 15)
        self.assertEqual(result, 2)

        result = calc_roi_one_period(2.5, 0)
        self.assertEqual(result, -1)

        result = calc_roi_one_period(6, 1)
        self.assertTrue(isinstance(result, float))

    def test_calc_pythagorean_theorem_side(self):
        """Tests for the right triangle side calculation."""

        result = calc_pythagorean_theorem_side(2, 5)
        self.assertEqual(result, 4.58258)

        result = calc_pythagorean_theorem_side(3, 5)
        self.assertEqual(result, 4)

        result = calc_pythagorean_theorem_side(6, 7)
        self.assertTrue(isinstance(result, float))

        result = calc_pythagorean_theorem_side(2, 2)
        self.assertTrue(isinstance(result, float))

    def test_calc_pythagorean_theorem_hyp(self):
        """Tests for the right triangle hypotenuse calculation"""

        result = calc_pythagorean_theorem_hyp(4, 5)
        self.assertEqual(result, 6.40312)

        result = calc_pythagorean_theorem_hyp(6, 1)
        self.assertEqual(result, 6.08276)

        result = calc_pythagorean_theorem_hyp(6, 1)
        self.assertTrue(isinstance(result, float))


unittest.main()
