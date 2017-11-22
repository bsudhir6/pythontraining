from pkg.MyInt import MyInt
import unittest

class MyTest(unittest.TestCase):
    def test_add(self):
        """Testing adding functionality"""
        a = MyInt(2)
        b = MyInt(3)
        self.assertEqual(a+b, MyInt(5))
    def test_less(self):
        """Testing less comparision functionality"""
        a = MyInt(2)
        b = MyInt(3)
        self.assertLess(a, b)
    def test_great(self):
        """Testing great comparision functionality"""
        a = MyInt(2)
        b = MyInt(3)
        self.assertGreater(a, b)
        
