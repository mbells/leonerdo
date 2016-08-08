import unittest

import gcoder

class GCoderTest(unittest.TestCase):

    def test_transform(self):
        g = gcoder.GCoder()
        g.input_bounds(0, 200, 100, 0)
        self.assertEqual(g.transform(0,0), (-65,65))
        self.assertEqual(g.transform(200,0), (65,65))
        self.assertEqual(g.transform(200,100), (65,-65))
        self.assertEqual(g.transform(0,100), (-65,-65))


if __name__ == '__main__':
    unittest.main()
