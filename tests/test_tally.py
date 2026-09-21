import unittest
from src.tracesum import summarize


class TestTally(unittest.TestCase):
    def test_lines_without_level_ignored(self):
        counts = summarize(["plain line", "x=1 nothing"])
        self.assertEqual(counts, {})


if __name__ == "__main__":
    unittest.main()
