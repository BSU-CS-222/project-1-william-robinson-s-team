import json
import ssl
from urllib.request import urlopen

def inputConversion(articleTitle):  #converts input article title into a wikipedia api url
    x = articleTitle.split()
    articleConversion = articleTitle.translate({ord(i): '%20' for i in ' '})
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=" + articleConversion + "&rvprop=timestamp|user&rvlimit=30&redirects"
    return url

def main():
    articleTitle = str(input("Please enter the title of the article: "))
    url = inputConversion(articleTitle)
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    changeData = json.loads(response.read())

    pageID = list(changeData['query']['pages'].keys())[0] #I couldn't find how on the API so I am brute forcing it >:)
    Revisions = changeData['query']['pages'][pageID]['revisions'] #gets the revision histor

    if(len(Revisions) >= 30): #Checks amount of revisions, if less than 30 we go by the length of the list
        for i in range(0, 29):
            print(Revisions[i]['timestamp'] + ' ' + Revisions[i]['user'] + '\n')
    
    else:
        for i in range(0, len(Revisions)):
            print(Revisions[i]['timestamp'] + ' ' + Revisions[i]['user'] + '\n')

main()