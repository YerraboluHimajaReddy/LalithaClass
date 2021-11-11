import unittest
class SignupTest(unittest.TestCase):
    
    def test_LoginByEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_LoginByFacebook(self):
        print("This is login by Facebook test")
        self.assertTrue(True)

    def test_LoginByTwitter(self):
        print("This is login by Twitter test")
        self.assertTrue(True)




if __name__=="__main__":
    unittest.main()

# Ran 3 tests in 0.022s
#
# OK
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test