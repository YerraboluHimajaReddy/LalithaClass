import unittest

from LalithaPythonClass.UnitTesting.Package1.LoginTest import LoginTest
from LalithaPythonClass.UnitTesting.Package1.SignupTest import SignupTest
from LalithaPythonClass.UnitTesting.Package2.PaymentReturnsTest import PaymentReturnsTest
from LalithaPythonClass.UnitTesting.Package2.PaymentTest import PaymentTest

# get all tests
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)


# creating test suite
sanityTestSuite=unittest.TestSuite([tc4,tc2])
sanityTestSuite1=unittest.TestSuite([tc3,tc1])
unittest.TextTestRunner().run(sanityTestSuite)
unittest.TextTestRunner().run(sanityTestSuite1)

print("===========================")
masterTestSuite=unittest.TestSuite([tc3,tc1,tc2,tc4])
unittest.TextTestRunner().run(masterTestSuite)

print("===========================")
functionalTestSuite=unittest.TestSuite([tc3,tc1,tc2])
unittest.TextTestRunner().run(functionalTestSuite)

# This is payment return by bank test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s
#
# OK
#
# Process finished with exit code 0
# This is payment return by bank test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
# This is payment in dollar test
# This is payment in rupees test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
#
# OK
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.002s
#
# OK
#
# Process finished with exit code 0
# .........
# ----------------------------------------------------------------------
# Ran 9 tests in 0.001s
#
# OK
# ===========================
# This is payment in dollar test
# This is payment in rupees test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
# This is payment return by bank test
# ===========================
#
# Process finished with exit code 0
# ........
# ----------------------------------------------------------------------
# Ran 8 tests in 0.002s
#
# OK
# ===========================
# This is payment in dollar test
# This is payment in rupees test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
# This is login by email test
# This is login by Facebook test
# This is login by Twitter test
#
# Process finished with exit code 0