import unittest

from wikiChanges import inputConversion
from wikiChanges import main

class wikiChangesTest(unittest.TestCase):
    def test_inputConversion(self):
        self.assertEqual(inputConversion("Ball State University"), "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Ball%20State%20University&rvprop=timestamp|user&rvlimit=30&redirects")
        #tests proper url creation

    def test_main(self):
        self.assertRaises(KeyError, main())

if __name__ == '__main__':
    unittest.main()