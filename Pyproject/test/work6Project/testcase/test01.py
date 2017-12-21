
import unittest


class test02(unittest.TestCase):
    def testAddNum(self):
        u'求和方法测试'
        self.assertEqual((1 + 2), 3)
        self.assertEqual((0 + 1), 1)
        print('########### test01')

    def testChengFa(self):
        u'乘法结果测试'
        self.assertEqual((0 * 8), 0)
        self.assertEqual((1 * 2), 3)


if __name__ == '__main__':
    unittest.main()
