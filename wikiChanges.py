import json
import ssl
from urllib.request import urlopen
import urllib.error

def inputConversion(articleTitle):  #converts input article title into a wikipedia api url
    articleConversion = articleTitle.translate({ord(i): '%20' for i in ' '})
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=" + articleConversion + "&rvprop=timestamp|user&rvlimit=30&redirects"
    return url

def main():
    articleTitle = str(input("Please enter the title of the article: "))

    try:
        url = inputConversion(articleTitle)
        context = ssl._create_unverified_context()
        response = urlopen(url, context=context)
        changeData = json.loads(response.read())
        #print(changeData)
    except urllib.error.URLError:      #network error exception
        print("Exit Code 3: Network Error")
        quit()

    
    try:    #check for lack of input or nonexistant title
        if changeData['batchcomplete'] == '':
            if articleTitle.isspace() or articleTitle == "":
                print("Exit Code 1: No User Input")
            else:
                print("Exit Code 2: Article Does Not Exist")

    except KeyError:    #run if user input exists AND matches an article title

        try:    #check for redirects
            print("Redirected from '" + str(changeData['query']['normalized'][0]['from']) + "' to '" + str(changeData['query']['normalized'][0]['to']) + "'.\n")
        except KeyError:
            print("")

        pageID = list(changeData['query']['pages'].keys())[0] #I couldn't find how on the API so I am brute forcing it >:)
        Revisions = changeData['query']['pages'][pageID]['revisions'] #gets the revision history

        if(len(Revisions) >= 30): #Checks amount of revisions, if less than 30 we go by the length of the list
            for i in range(0, 29):
                print(Revisions[i]['timestamp'] + ' ' + Revisions[i]['user'] + '\n')
    
        else:
            for i in range(0, len(Revisions)):
                print(Revisions[i]['timestamp'] + ' ' + Revisions[i]['user'] + '\n')
        
main()