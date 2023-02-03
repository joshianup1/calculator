

from tkinter import *


root = Tk()
root.title("Calculator")

ent = Entry(root, width=35, borderwidth=5)
ent.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 


def clickButton(number):
    current = ent.get()
    ent.delete(0, END)
    ent.insert(0, str(current) + str(number))


def clearButton():
    ent.delete(0, END)


def button_add():
    first_number = ent.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    ent.delete(0, END)

def button_sub():
    first_number = ent.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    ent.delete(0, END)  

def button_div():
    first_number = ent.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    ent.delete(0, END)   

def button_mul():
    first_number = ent.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    ent.delete(0, END) 

def button_per():
    first_number = ent.get()
    ent.delete(0,END)
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    ent.delete(0, END)  


def equalButton():
    secondNum = ent.get()
    ent.delete(0,END)
    if math == "addition":
        ent.insert(0, int(f_num) + int(secondNum))
    elif math == "substraction":
        ent.insert(0,int(f_num) - int(secondNum))    
    elif math == "division":
        ent.insert(0,int(f_num) / int(secondNum))  
    elif math == "multiplication":
        ent.insert(0,int(f_num) * int(secondNum))  
    elif math == "percentage":
        if ent.insert == (f_num) / int(secondNum):
            return ent.insert*100



    


# this defines the buttons
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: clickButton(1)) # the first button of the calculator
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: clickButton(2)) # the second button of the calculator
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: clickButton(3)) # the third button of the calculator
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: clickButton(4)) # the fourth button of the calculator
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: clickButton(5)) # the fifth button of the calculator
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: clickButton(6)) # the sixth  button of the calculator
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: clickButton(7)) # the seventh button of the calculator
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: clickButton(8)) # the eighth button of the calculator
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: clickButton(9)) # the ninth button of the calculator
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: clickButton(0)) # the tenth button of the calculator
#button_addition = Button(root, text="+", padx=40, pady=20, command=lambda:button_add('+')) # addition button
buttonAdd = Button(root, text="+", padx=40, pady=20, command=lambda: button_add())
button_equalSign = Button(root, text="=", padx=40, pady=20, command=lambda: equalButton()) # button for the equal sign
button_clr = Button(root, text="Clear", padx=30, pady=20, command=lambda: clearButton()) #button for clearing whatever is written
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_div())
# this puts the buttons on the screen
minusButton = Button(root, text="-", padx=40, pady=20, command=lambda: button_sub())
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_mul())
button_percentage = Button(root, text="%", padx=40, pady=20, command=lambda: button_per())


#row 3
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

# row 2
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

# row 1
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

# sign buttons
button0.grid(row=4, column=0)
button_clr.grid(row=4, column=1)
buttonAdd.grid(row=4, column=2)

#row 5
button_multiply.grid(row=5,column=0)
button_divide.grid(row=5,column=1)
minusButton.grid(row=5,column=2)
button_equalSign.grid(row=6, column=0)
button_percentage.grid(row=6,column=1)



root.mainloop()

