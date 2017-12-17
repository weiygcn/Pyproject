
import unittest


class test02(unittest.TestCase):
    def testAdd(self):
        self.assertEqual((1 + 2), 3)
        self.assertEqual((0 + 1), 1)

    def testChengFa(self):
        self.assertEqual((0 * 8), 0)
        self.assertEqual((1 * 2), 3)


if __name__ == '__main__':
    unittest.main()
