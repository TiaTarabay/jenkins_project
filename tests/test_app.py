 # tests/test_app.py
from os import name
import unittest
from app import greet
class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"),"Hello, World fromTia Tarabay!")

if name == "__main__":
    unittest.main()