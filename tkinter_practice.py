from tkinter import *

root = Tk()

myLabel = Label(root , text = "Hello world") #Label takes in two arguements, where the widget should be located and the text it will comprise of.
myLabel2 = Label(root, text = "What's up my people?")

myLabel.grid(row = 0, column= 0)
myLabel2.grid(row= 0, column= 1)

root.mainloop()