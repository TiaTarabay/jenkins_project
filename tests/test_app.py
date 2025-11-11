# tests/test_app.py
import unittest
import os
import sys
sys.path.append(os.getcwd())

from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
