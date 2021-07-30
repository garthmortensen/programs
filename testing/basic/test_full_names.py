import unittest
from full_names import get_full_name  # pointer


class NamesTestCast(unittest.TestCase):
    """Tests for name.py.
    p.s. - Never update your test to make things work. Update your code!"""

    def test_first_last(self):
        """Test names like Goat Mortensen"""

        full_name = get_full_name("pony", "mortensen")
        self.assertEqual(full_name, "Pony Mortensen")

        full_name = get_full_name("goat", "mortensen")
        self.assertEqual(full_name, "Goat Mortensen")


    def test_first_last_middle(self):
        """Test names like Goat Mortensen"""

        full_name = get_full_name("pony", "mortensen", "sweetie")
        self.assertEqual(full_name, "Pony Sweetie Mortensen")

        full_name = get_full_name("goat", "mortensen", "studman")
        self.assertEqual(full_name, "Goat Studman Mortensen")


unittest.main()
