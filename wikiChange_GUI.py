import tkinter as tk
import tkinter.scrolledtext as st

from wikiChanges_funcs import *

root = tk.Tk()
root.title("Wikipedia Revision Search")
root.geometry("500x550")

def GUI():
    wikiTitle = tk.StringVar()

    wikiTitleLabel = tk.Label(root, text="Enter Wikipedia Article Title: ")
    wikiTitleEntry = tk.Entry(root, textvariable=wikiTitle)
    redirectLabel = tk.Label(root, text="")

    wikiTitleLabel.pack()
    wikiTitleEntry.pack()

    wikiRevisionBox = st.ScrolledText(root, width = 60, height = 25, font=("Helvetica", 10))

    printButton = tk.Button(root, text="Print Revisions", command=lambda: GUI_PrintRevisions(wikiTitle.get(), wikiRevisionBox, redirectLabel))
    printButton.pack()
    
    root.mainloop()

def GUI_PrintRevisions(title, wikiRevisionBox, redirectLabel):
    changeData = URLErrorExceptionCheck(title)
    wikiRevisionBox.delete("1.0", "end") #reset contents of scrolled text box
    redirectLabel.config(text = "")

    if changeData == "Error Code 3: Network Error":   #exit program if there is a network error
        wikiRevisionBox.insert(tk.INSERT, changeData)
        wikiRevisionBox.pack()

    try:    #check for lack of input or nonexistant title
        errorCode = invalidInputCheck(changeData, title)
        if errorCode == "Error Code 1: No User Input":
            wikiRevisionBox.insert(tk.INSERT, errorCode)
        else:
            wikiRevisionBox.insert(tk.INSERT, errorCode)
        wikiRevisionBox.pack()
        
    
    except KeyError:    #run if user input exists AND matches an article title
        redirect = redirectCheckGUI(changeData)
        redirectLabel.config(text = redirect)
        redirectLabel.pack()
        Revisions = getRevisions(changeData)
        
        for i in Revisions:
            wikiRevisionBox.insert(tk.INSERT, i['timestamp'] + ' ' + i['user'] + '\n')
            #NOTE: Do NOT use sleep to test for the GUI. It will freeze the GUI.
        wikiRevisionBox.pack()

    except TypeError:
        return

GUI()