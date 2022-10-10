# coding = utf-8
import unittest
class FistCase01(unittest.TestCase):  #继承于unittest.TestCase

    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print("这是case的后置条件")

    @unittest.skip("不执行第1条case")
    def test001(self):
        print("第01条case")

    def test002(self):
        print("第02条case")

    def test003(self):
        print("第03条case")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FistCase01('test002'))
    suite.addTest(FistCase01('test001'))
    suite.addTest(FistCase01('test003'))
    # suite.addTest(FistCase01('testFist02'))
    unittest.TextTestRunner().run(suite)
    # unittest.main()  运行要用unittest.main()





