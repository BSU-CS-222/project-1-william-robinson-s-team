import json
import ssl
from urllib.request import urlopen
import urllib.error

def inputConversion(articleTitle):  #converts input article title into a wikipedia api url
    articleUpper = articleTitle.title()
    articleConversion = articleUpper.translate({ord(i): '%20' for i in ' '})
    url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&titles=" + articleConversion + "&rvprop=timestamp|user&rvlimit=30&redirects"
    return url

def URLErrorExceptionCheck(articleTitle):   #check for network errors
    try:
        url = inputConversion(articleTitle)
        context = ssl._create_unverified_context()
        response = urlopen(url, context=context)
        changeData = json.loads(response.read())
        return changeData
    except urllib.error.URLError or urllib.error.HTTPError:      
        errorCode = "Error Code 3: Network Error"
        print(errorCode)
        return errorCode

def invalidInputCheck(changeData, articleTitle):       #checks for lack of user input or non-existant article titles
    if changeData['batchcomplete'] == '':
            if articleTitle.isspace() or articleTitle == "":
                errorCode = "Error Code 1: No User Input"
                print(errorCode)
                return errorCode
                
            else:
                errorCode = "Error Code 2: Article: '" + articleTitle + "' Does Not Exist"
                print(errorCode)
                return errorCode
                

def redirectCheck(changeData):     #checks for any redirects
    try:    
        print("\nRedirected from '" + str(changeData['query']['normalized'][0]['from']) + "' to '" + str(changeData['query']['normalized'][0]['to']) + "'.\n")
    except KeyError:
        print("")

def printRevisions(changeData):             #prints the list of revisions
    pageID = list(changeData['query']['pages'].keys())[0] #gets the page id
    Revisions = changeData['query']['pages'][pageID]['revisions'] #gets the revision history

    if(len(Revisions) >= 30): #Checks amount of revisions, if less than 30, go by the length of the list
        for i in range(0, 30):
            print(Revisions[i]['timestamp'] + ' ' + Revisions[i]['user'] + '\n')
    
    else:
        for i in range(0, len(Revisions)):
            print(Revisions[i]['timestamp'] + ' ' + Revisions[i]['user'] + '\n')
    return Revisions