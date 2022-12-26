from tkinter import *

root = Tk()
root.title('Simple Calculator' )

e = Entry(root, width = 35,borderwidth=5 )
e.grid(row =0,column =0, columnspan = 3, padx = 10, pady = 10)

def quad_func():
    a = a.get()
    global math
    math = 'quad'
    a.insert(0, " a = " + str(a))
    


def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

    
    
def clear():
    e.delete(0, END)

def addition():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(float(first_number))
    e.delete(0, END)


    
def equal():
    second_number = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,f_num + int(float(second_number)))
    if math == 'subtraction':
        e.insert(0,f_num - int(float(second_number)))
    if math == 'multiplication':
        e.insert(0,f_num * int(float(second_number)))
    if math == 'division':
        e.insert(0,f_num / int(float(second_number)))
        
    
def subtraction():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(float(first_number))
    e.delete(0, END)
    
def multiplication():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(float(first_number))
    e.delete(0, END)

def division():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(float(first_number))
    e.delete(0, END)
    
    

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
div_button = Button(root, text='/',padx =40, pady = 30 , command=division)
sub_button = Button(root, text='-',padx =40, pady = 30 , command=subtraction)
button_equals = Button(root, text='=',padx =39, pady = 30, command= equal  )
times_button = Button(root, text='x',padx =39, pady = 30 , command=multiplication)
button_clear = Button(root, text='Clear',padx =77, pady = 30, command = clear)
quad_function = Button(root, text='quad func',padx =94, pady = 30, command = lambda:quad_func_btn())


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
div_button.grid(row = 6, column = 0)
times_button.grid(row = 6, column = 1)
sub_button.grid(row = 6, column = 2)
quad_function.grid(row = 7, column = 0, columnspan = 3)







root.mainloop()






# from tkinter import *
# import math

# def solve_quadratic():
#     # Get the coefficient values from the input fields
#     a = float(entry_a.get())
#     b = float(entry_b.get())
#     c = float(entry_c.get())

#     # Calculate the discriminant
#     discriminant = b**2 - 4*a*c

#     # Check if the quadratic has real solutions
#     if discriminant < 0:
#         result_label.config(text="The quadratic has no real solutions.")
#     elif discriminant == 0:
#         # Calculate the single solution
#         x = (-b + math.sqrt(discriminant)) / (2*a)
#         result_label.config(text=f"The quadratic has a single solution: {x:.2f}")
#     else:
#         # Calculate the two solutions
#         x1 = (-b + math.sqrt(discriminant)) / (2*a)
#         x2 = (-b - math.sqrt(discriminant)) / (2*a)
#         result_label.config(text=f"The quadratic has two solutions: {x1:.2f} and {x2:.2f}")

# # Create the main window
# root = Tk()
# root.title("Quadratic Equation Solver")

# # Create the input fields for the coefficients
# entry_a = Entry(root, width=5)
# entry_b = Entry(root, width=5)
# entry_c = Entry(root, width=5)

# # Create a label for the result
# result_label = Label(root, text="Enter the coefficients and press 'Solve' to find the solutions.")

# # Create a button to solve the quadratic
# solve_button = Button(root, text="Solve", command=solve_quadratic)

# # Add the widgets to the window
# entry_a.pack()
# entry_b.pack()
# entry_c.pack()
# result_label.pack()
# solve_button.pack()

# # Run the main loop
# root.mainloop()
