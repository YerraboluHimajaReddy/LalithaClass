def test_1():
   x=10
   y=10
   assert x==y

def test_2():
   name="mantri"
   title="lalitha mantri"
   assert name in title

def test_3():
   name="jenkins"
   title="Jenkins in CI/CD tool"
   assert name in title # AssertionError: assert 'jenkins' in 'Jenkins in CI/CD tool'
