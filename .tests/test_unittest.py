import inc_dec as indc      # The code to test
import unittest as ut       # The test framework

class Test_TestIncrementDecrement(ut.TestCase):

    def test_increment(self):
        self.assertAlmostEqual(indc.increment(3), 4)
    
    def funcname(self):
        self.assertAlmostEqual(indc.decrement(3), 4)


if __name__ == "__main__":
    ut.main()
