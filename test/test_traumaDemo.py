
import unittest
import traumaDemo

class TestDemo(unittest.TestCase):

    def test_readFiles(self):
        case1 = traumaDemo.readFiles(1)
        self.assertEqual(case1, "Depression_male3_JB.wav")
    
    def test_findFormants(self):

        if __name__ == '__main__':
            unittest.main()
