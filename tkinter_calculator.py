from tkinter import *

root = Tk()
root.title('Simple Calculator' )

e = Entry(root, width = 35,borderwidth=5 )
e.grid(row =0,column =0, columnspan = 3, padx = 10, pady = 10)


def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def clear():
    e.delete(0, END)

def addition():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    
def equal():
    second_number = e.get
    s_num = int(second_number)
    result = f_num + s_num
    e.delete(0,END)
    e.insert(0,result)
    
    

button_1 = Button(root, text='1',padx = 40, pady = 30,command = lambda: button_add(1))
button_2 = Button(root, text='2',padx = 40, pady = 30,command = lambda: button_add(2))
button_3 = Button(root, text='3',padx = 40, pady = 30,command = lambda: button_add(3))
button_4 = Button(root, text='4',padx = 40, pady = 30,command =lambda: button_add(4))
button_5 = Button(root, text='5',padx = 40, pady = 30,command = lambda:button_add(5))
button_6 = Button(root, text='6',padx = 40, pady = 30,command =lambda: button_add(6))
button_7 = Button(root, text='7',padx = 40, pady = 30,command = lambda:button_add(7))
button_8 = Button(root, text='8',padx = 40, pady = 30,command = lambda:button_add(8))
button_9 = Button(root, text='9',padx = 40, pady = 30,command = lambda:button_add(9))
button_0 = Button(root, text='0',padx = 40, pady = 30,command = lambda:button_add(0))
add_button = Button(root, text='+',padx =84, pady = 30 , command=addition)
button_equals = Button(root, text='=',padx =39, pady = 30 , command= equal)
button_times = Button(root, text='x',padx =39, pady = 30)
button_clear = Button(root, text='Clear',padx =77, pady = 30, command = clear)


button_1.grid(row =3, column =0 )
button_2.grid(row =3 , column =1 )
button_3.grid(row =3 , column =2 )

button_4.grid(row =2 , column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column =2 )

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column =1 )
button_9.grid(row = 1, column =2 )

button_0.grid(row =4 , column =0 )

add_button.grid(row = 4, column = 1, columnspan = 2)
button_equals.grid(row = 5, column = 0)
button_clear.grid(row = 5, column = 1 , columnspan = 2)







root.mainloop()