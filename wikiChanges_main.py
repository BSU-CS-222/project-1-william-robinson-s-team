from wikiChanges_funcs import URLErrorExceptionCheck, invalidInputCheck, redirectCheck, printRevisions

def main():
    articleTitle = str(input("Please enter the title of the article: "))

    changeData = URLErrorExceptionCheck(articleTitle)

    if changeData == "Error Code 3: Network Error":
        quit()
    
    try:    #check for lack of input or nonexistant title
        invalidInputCheck(changeData, articleTitle)

    except KeyError:    #run if user input exists AND matches an article title
        redirectCheck(changeData)
        printRevisions(changeData)
        
main()