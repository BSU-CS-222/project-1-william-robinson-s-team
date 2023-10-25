import tkinter as tk

from wikiChanges_funcs import *

def GUI():
    root = tk.Tk()
    root.title("Wikipedia Revision Search")
    root.geometry("500x500")

    wikiTitle = tk.StringVar()

    wikiTitleLabel = tk.Label(root, text="Enter Wikipedia Article Title: ")
    wikiTitleEntry = tk.Entry(root, textvariable=wikiTitle)

    wikiTitleLabel.grid(row=0, column=0)
    wikiTitleEntry.grid(row=0, column=1)

    printButton = tk.Button(root, text="Print Revisions", command=lambda: GUI_PrintRevisions(wikiTitle.get()))
    printButton.grid(row=1, column=0)





    root.mainloop()

def GUI_PrintRevisions(title):
    changeData = URLErrorExceptionCheck(title)

    if changeData == "Error Code 3: Network Error":   #exit program if there is a network error
        quit()

    try:    #check for lack of input or nonexistant title
        invalidInputCheck(changeData, title)
    
    except KeyError:    #run if user input exists AND matches an article title
        redirectCheck(changeData)
        printRevisions(changeData)
        print("Error Code 0: Exitting")
    



GUI()