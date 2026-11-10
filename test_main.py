"""Tests for EvmTxCostAnalyzer."""
import unittest
from main import calculate


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertAlmostEqual(calculate(60000, 5), 0.0003, places=6)


if __name__ == "__main__":
    unittest.main()
