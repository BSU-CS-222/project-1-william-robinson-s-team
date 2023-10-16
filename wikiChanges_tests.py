import unittest

from wikiChanges import inputConversion

class wikiChangesTest(unittest.TestCase):
    def test_inputConversion(self):
        self.assertEqual(inputConversion("Ball State University"), "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Ball%20State%20University%20&rvprop=timestamp|user&rvlimit=30&redirects")

if __name__ == '__main__':
    unittest.main()