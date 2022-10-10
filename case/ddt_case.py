import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这是一个前置")
    def tearDown(self):
        print("这是一个后置")
    # 1,2 3,4 5,6
    @ddt.data(
        [1,2],
        ["3","4"],
        [5,6]
    )
    @ddt.unpack
    def testAdd(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()