#Random Quote Generator

#tkinter for a GUI
#Need to find a quote API
#setup Github Repo - DONE


import tkinter as tk
import requests



root = tk.Tk()
root.configure()


root = tk.Tk()
root.configure(background = "white")
root.title("Random Quote Practice")
root.geometry("500x500")
#first name last name address city state zip phone number hourly rate normal hours
#save clear close
#first name
entry1 = tk.Entry(root, bg="white")
label1 = tk.Label(root, text="First Name", bg="grey")




#save button
btnSave = tk.Button(root, text="Save")
#clear button
btnClear = tk.Button(root, text="Clear")
#close button
btnClose = tk.Button(root,text="Close")


#Screen elements placement

#first name place
entry1.place(x=200, y=25)
label1.place(x=10, y=25)

#save place
btnSave.place(x=10, y=400)
#clear place
btnClear.place(x=155, y=400)

#close place
btnClose.place(x=300, y=400)
root.mainloop()
