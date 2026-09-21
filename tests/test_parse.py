import unittest
from src.tracesum import summarize


class TestParse(unittest.TestCase):
    def test_counts_level_fields(self):
        counts = summarize(["level=info ok", "level=error boom", "level=error retry"])
        self.assertEqual(counts, {"info": 1, "error": 2})


if __name__ == "__main__":
    unittest.main()
