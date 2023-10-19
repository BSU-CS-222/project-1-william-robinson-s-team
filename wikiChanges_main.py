from wikiChanges_funcs import URLErrorExceptionCheck, invalidInputCheck, redirectCheck, printRevisions

def main():
    articleTitle = str(input("Please enter the title of the article: "))

    changeData = URLErrorExceptionCheck(articleTitle)     #convert article title to api url, check for network error, and retrieve data

    if changeData == "Error Code 3: Network Error":   #exit program if there is a network error
        quit()
    
    try:    #check for lack of input or nonexistant title
        invalidInputCheck(changeData, articleTitle)

    except KeyError:    #run if user input exists AND matches an article title
        redirectCheck(changeData)
        printRevisions(changeData)
        print("Error Code 0: Exitting")
        
main()