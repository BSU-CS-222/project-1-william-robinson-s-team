import json
import ssl
from urllib.request import urlopen

def inputConversion(articleTitle):
    x = articleTitle.split()
    articleConversion = ""
    for y in x:
        articleConversion += y + "%20"
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=" + articleConversion + "&rvprop=timestamp|user&rvlimit=30&redirects"
    return url

def main():
    articleTitle = str(input("Please enter the title of the article: "))
    url = inputConversion(articleTitle)
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    changeData = json.loads(response.read())
    print(changeData)

main()