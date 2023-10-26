import tkinter as tk
import time

from wikiChanges_funcs import *

root = tk.Tk()
root.title("Wikipedia Revision Search")
root.geometry("500x500")

def GUI():
    

    wikiTitle = tk.StringVar()

    wikiTitleLabel = tk.Label(root, text="Enter Wikipedia Article Title: ")
    wikiTitleEntry = tk.Entry(root, textvariable=wikiTitle)

    wikiTitleLabel.pack()
    wikiTitleEntry.pack()

    printButton = tk.Button(root, text="Print Revisions", command=lambda: GUI_PrintRevisions(wikiTitle.get()))
    printButton.pack()

    root.mainloop()

def GUI_PrintRevisions(title):
    changeData = URLErrorExceptionCheck(title)

    if changeData == "Error Code 3: Network Error":   #exit program if there is a network error
        quit()

    try:    #check for lack of input or nonexistant title
        invalidInputCheck(changeData, title)
    
    except KeyError:    #run if user input exists AND matches an article title
        redirectCheck(changeData)
        Revisions = printRevisions(changeData)
        for i in Revisions:
            wikiRevisionLabel = tk.Label(root, text=i['timestamp'] + ' ' + i['user'] + '\n', font=("Helvetica", 5))
            wikiRevisionLabel.pack()

            #NOTE: Do NOT use sleep to test for the GUI. It will freeze the GUI.
        

        print("Error Code 0: Exitting")

GUI()