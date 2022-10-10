# coding = utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def testCase01 (self):
        #casePath = os.path.join(os.getcwd(),'case')
        casePath = os.path.join(os.getcwd())
        print(casePath)
        #suite = unittest.defaultTestLoader.discover('../case','unittest_*.py')
        suite = unittest.defaultTestLoader.discover(casePath, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()