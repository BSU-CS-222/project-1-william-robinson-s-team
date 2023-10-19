import unittest
import urllib.error

from wikiChanges_funcs import inputConversion, URLErrorExceptionCheck, invalidInputCheck, redirectCheck, printRevisions

class wikiChanges_tests(unittest.TestCase):
    def test_inputConversion(self):
        articleTitle = "Ball State University"
        self.assertEqual(inputConversion(articleTitle), "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=Ball%20State%20University&rvprop=timestamp|user&rvlimit=30&redirects")
        #tests proper url creation

    def test_blankInput(self):   #tests lack of user input
        articleTitle = ""
        changeData = {"batchcomplete":""}
        self.assertEqual(invalidInputCheck(changeData, articleTitle), "Error Code 1: No User Input")

    def test_nonexistantArticle(self):     #tests artilce title that doesn't exist
        articleTitle = "efsfsegsfgdg"
        changeData = {"batchcomplete":""}
        self.assertEqual(invalidInputCheck(changeData, articleTitle), "Error Code 2: Article: '" + articleTitle + "' Does Not Exist")
            

if __name__ == '__main__':
    unittest.main()