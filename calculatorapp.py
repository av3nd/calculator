# importing modules
# --------------------------------------------------------------------------------------------------------------------
from tkinter import *
from _ast import Lambda


# creating window putting icon and background
# --------------------------------------------------------------------------------------------------
root = Tk()
root.title("Calculator")
root.iconbitmap('calculator.ico')
root.geometry("345x530")
root.minsize(345,530)
root.maxsize(345,530)
bg = PhotoImage(file="STAR.png")
my_label = Label(root, image = bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)




# Creating entry for calculator
# ----------------------------------------------------------------------------------------------------------
e = Entry(root, width=50, borderwidth=10)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)


# functions used by buttons
# ------------------------------------------------------------------------------------------
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))


def button_clear():
    e.delete(0, END)




def button_add():
    first_number = e.get()
    global f_num
    global function
    function = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global function
    function = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global function
    function = "div"
    f_num = int(first_number)
    e.delete(0, END)

def button_mul():
    first_number = e.get()
    global f_num
    global function
    function = "mul"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if function == "add":
        e.insert(0,f_num + int(second_number))
    elif function == "sub":
        e.insert(0,f_num - int(second_number))
    elif function == "mul":
        e.insert(0,f_num * int(second_number))
    elif function == "div":
        e.insert(0,f_num / int(second_number))

# button design
# ---------------------------------------------------------------------------------------------------
button1 = Button(root, text="1", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(1))
button2 = Button(root, text="2", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(2))
button3 = Button(root, text="3", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(3))
button4 = Button(root, text="4", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(4))
button5 = Button(root, text="5", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(5))
button6 = Button(root, text="6", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(6))
button7 = Button(root, text="7", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(7))
button8 = Button(root, text="8", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(8))
button9 = Button(root, text="9", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(9))
button0 = Button(root, text="0", padx=40, pady=20,bg='black', fg = 'white',font=20, command=lambda : button_click(0))
button_add = Button(root, text="+", padx=40, pady=20,bg='black', fg = 'yellow',font=20, command=button_add)
button_equal = Button(root, text="=", padx=85, pady=20,bg='black', fg = 'yellow',font=20, command=button_equal)
button_clear = Button(root, text="clear", padx=69, pady=20,bg='black', fg = 'yellow',font=20, command=button_clear)
button_div = Button(root, text="%", padx=40, pady=20,bg='black', fg = 'yellow',font=20, command=button_div)
button_sub = Button(root, text="-", padx=40, pady=20,bg='black', fg = 'yellow',font=20, command=button_sub)
button_mul = Button(root, text="X", padx=40, pady=20,bg='black', fg = 'yellow',font=20, command=button_mul)
# Button placement
# ------------------------------------------------------------------------------------------
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)

button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)

button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
button0.grid(row=4, column=1)

button_add.grid(row=5, column=1)
button_equal.grid(row=4, column=2, columnspan=2)
button_clear.grid(row=5, column=2, columnspan=2)

button_div.grid(row=6,column=1)
button_mul.grid(row=6,column=2)
button_sub.grid(row=6,column=3)

root.mainloop()