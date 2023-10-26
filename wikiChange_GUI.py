import tkinter as tk
import tkinter.scrolledtext as st
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
    wikiRevisionBox = st.ScrolledText(root, width = 60, height = 25, font=("Helvetica", 10))

    if changeData == "Error Code 3: Network Error":   #exit program if there is a network error
        wikiRevisionBox.insert(tk.INSERT, changeData)

    try:    #check for lack of input or nonexistant title
        invalidInputCheck(changeData, title)
    
    except KeyError:    #run if user input exists AND matches an article title
        redirectCheck(changeData)
        Revisions = printRevisions(changeData)
        
        for i in Revisions:
            wikiRevisionBox.insert(tk.INSERT, i['timestamp'] + ' ' + i['user'] + '\n')
            #NOTE: Do NOT use sleep to test for the GUI. It will freeze the GUI.
        wikiRevisionBox.pack()
        

        print("Error Code 0: Exitting")

GUI()