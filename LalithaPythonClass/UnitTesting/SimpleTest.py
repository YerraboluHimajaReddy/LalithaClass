import unittest
class SimpleTest(unittest.TestCase):
    # Returns True or False.

    def test(self):
        self.assertTrue(True)
        print("=============")
    def test_number(self):
        x=10
        y=20
        self=x+y;
        print("self value is :", self)
    def test_multipllication(self):
        x=10
        y=20
        #self=x*y;
        print("Multtioniplica value is :", x*y)


if __name__ == '__main__':
    unittest.main()
