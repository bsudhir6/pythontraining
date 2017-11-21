from pkg.MyInt import MyInt 

import unittest 


class MyTest(unittest.TestCase):
    def test_add(self):
        '''testing add functionality'''
        a = MyInt(1)
        b = MyInt(2)
        self.assertEqual(a + b , MyInt(3))
    def test_less(self):
        '''testing less than  functionality'''
        a = MyInt(1)
        b = MyInt(2)
        self.assertLess(a,b)