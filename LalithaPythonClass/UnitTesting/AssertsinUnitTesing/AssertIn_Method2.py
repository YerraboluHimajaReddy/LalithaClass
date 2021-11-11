import unittest


class Himaja(unittest.TestCase):

    # test function to test whether key is present in container
    def test_negative(self):
        key = "Himaja"
        container = "Himaja reddy yerrabolu"
        # error message in case if test case got failed
        message = "key is not in container."
        # assertIn() to check if key is in container
        self.assertIn(key, container, message)


if __name__ == '__main__':
    unittest.main()

# AssertionError: 'lalitha' not found in 'Himaja reddy yerrabolu' : key is not in container.