from tkinter import *

root = Tk()

myLabel = Label(root , text = "Hello world") #Label takes in two arguements, where the widget should be located and the text it will comprise of.
myLabel.grid(row = 0, column= 1)


#tkinter grid system
def clickme():
    myLabel2 = Label(root, text = "What's up my people?")
    myLabel2.grid(row = 0, column= 0)


# Creating buttons
my_button = Button(root, text = "Click me!!!!", padx=50, pady=20, command= clickme, fg="red").grid(row = 0, column=1)
#  The "command" arguement is always used to call a function to a method it is assigned to.
#  The "fg" arguement changes color while the "bg" arguement changes the background color
# my_button.pack() # Cannot use pack method while there is another action  being performed with the grid function.

# INPUT FIELDS
e = Entry(root)
e.grid(row= 0, column = 0)



root.mainloop()