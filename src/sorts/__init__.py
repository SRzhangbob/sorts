import sorts.singleton_model
import sorts.testsingleton
import unittest

class UnitTest1(unittest.TestCase):
    # __slots__ = ['a']
    def test_Try(self):
        self.assertIs(sorts.singleton_model.singleton, sorts.testsingleton.c)

if __name__ == "__main__":
    unittest.main()
