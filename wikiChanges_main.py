from wikiChanges_funcs import *
from sys import exit

def main():
    articleTitle = str(input("Please enter the title of the article: "))

    changeData = URLErrorExceptionCheck(articleTitle)     #convert article title to api url, check for network error, and retrieve data

    if changeData == "Error Code 3: Network Error":   #exit program if there is a network error
        exit(3)
    
    try:    #check for lack of input or nonexistant title
        errorCode = invalidInputCheck(changeData, articleTitle)
        if errorCode == "Error Code 1: No User Input":
            print(errorCode)
            exit(1)
        elif errorCode == "Error Code 2: Article: '" + articleTitle + "' Does Not Exist":
            print(errorCode)
            exit(2)
            

    except KeyError:    #run if user input exists AND matches an article title
        redirectCheckMain(changeData)
        Revisions = getRevisions(changeData)
        printRevisions(Revisions)
        print("Error Code 0: Exitting")
        
main()