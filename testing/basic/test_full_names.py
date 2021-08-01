import unittest
from full_names import get_full_name  # pointer


class NamesTestCast(unittest.TestCase):
    """Tests for name.py.
    p.s. - Never update your test to make things work. Update your code!"""

    def test_first_last(self):
        """Test names like Goat Cat"""

        full_name = get_full_name("pony", "cat")
        self.assertEqual(full_name, "Pony Cat")

        full_name = get_full_name("goat", "cat")
        self.assertEqual(full_name, "Goat Cat")


    def test_first_last_middle(self):
        """Test names like Goat Studman Cat"""

        full_name = get_full_name("pony", "cat", "sweetie")
        self.assertEqual(full_name, "Pony Sweetie Cat")

        full_name = get_full_name("goat", "cat", "studman")
        self.assertEqual(full_name, "Goat Studman Cat")


unittest.main()
