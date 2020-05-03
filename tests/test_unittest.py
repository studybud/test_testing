import inc_dec as indc      # The code to test
import unittest as ut       # The test framework

class Test_TestIncrementDecrement(ut.TestCase):

    def test_increment(self):
        self.assertEqual(indc.increment(3), 4)
    
    def test_decrement(self):
        self.assertEqual(indc.decrement(5), 4)
    
    # will always fail
    def test_failure(self):
        self.assertAlmostEqual(True, False)


if __name__ == "__main__":
    ut.main()
