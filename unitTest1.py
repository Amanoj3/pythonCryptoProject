import unittest
import appOperations

class MyTestCase(unittest.TestCase):
    def test_fileValidity(self):
        self.assertEqual(appOperations.filenameValid("abc.csv"), True)
        self.assertEqual(appOperations.filenameValid("xyz.csv"), False)


if __name__ == '__main__':
    unittest.main()
