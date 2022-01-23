import tkinter as tk
from tkinter import messagebox


expression = ""

root = tk.Tk()
root.geometry("390x440")
root.minsize(390, 440)
root.maxsize(390, 440)

equation = tk.StringVar()
equation_result = tk.StringVar()
equation_result.set("0")


def click(text):

    global expression
    expression += str(text)

    equation.set(expression)


def deletecharacter():

    global expression
    expression = expression[:-1]

    equation.set(expression)


def clearpress():

    global expression
    expression = ""
    equation.set("")
    equation_result.set("0")


def pressnegative():
    messagebox.showinfo("I'm Lazy", "Is not implemented")


def clickequal():

    global expression

    try:
        expression = str(eval(expression))

        equation_result.set(expression)
        expression = ""
        equation.set(expression)

    except:
        equation.set("Error: Wrong Input")
        expression = ""


def driver():

    expression_field_frame = tk.Frame(root, width=233, height=85, relief='solid', bg="grey")
    expression_field_frame.grid(columnspan=3)
    expression_field_frame.pack_propagate(False)

    expression_field_label1 = tk.Entry(expression_field_frame, text=equation_result, font="Helvetica 15", width="20",
                                       relief="groove", justify='right', bg="#C6C6C6")
    expression_field_label1.grid(columnspan=3, row=0)

    expression_field_label2 = tk.Entry(expression_field_frame, text=equation, font="Helvetica 15", width="20",
                                       relief="groove", justify='right')
    expression_field_label2.grid(columnspan=3, row=1, ipady="8")

    number_0 = tk.Button(root, text="0", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(0))
    number_0.grid(row=4, column=1)

    number_1 = tk.Button(root, text="1", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(1))
    number_1.grid(row=1, column=0)

    number_2 = tk.Button(root, text="2", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(2))
    number_2.grid(row=1, column=1)

    number_3 = tk.Button(root, text="3", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(3))
    number_3.grid(row=1, column=2)

    number_4 = tk.Button(root, text="4", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(4))
    number_4.grid(row=2, column=0)

    number_5 = tk.Button(root, text="5", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(5))
    number_5.grid(row=2, column=1)

    number_6 = tk.Button(root, text="6", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(6))
    number_6.grid(row=2, column=2)

    number_7 = tk.Button(root, text="7", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(7))
    number_7.grid(row=3, column=0)

    number_8 = tk.Button(root, text="8", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(8))
    number_8.grid(row=3, column=1)

    number_9 = tk.Button(root, text="9", width=4, height=2, font='Helvetica 20 bold', command=lambda: click(9))
    number_9.grid(row=3, column=2)

    dot = tk.Button(root, text=".", width=4, height=2, font='Helvetica 20 bold', command=lambda: click("."))
    dot.grid(row=4, column=2)

    divide = tk.Button(root, text="/", width=4, height=2, font='Helvetica 20 bold', command=lambda: click("/"))
    divide.grid(row=1, column=4)

    multiply = tk.Button(root, text="*", width=4, height=2, font='Helvetica 20 bold', command=lambda: click("*"))
    multiply.grid(row=1, column=3)

    plus = tk.Button(root, text="+", width=4, height=2, font='Helvetica 20 bold', command=lambda: click("+"))
    plus.grid(row=2, column=3)

    minus = tk.Button(root, text="-", width=4, height=2, font='Helvetica 20 bold', command=lambda: click("-"))
    minus.grid(row=2, column=4)

    equal = tk.Button(root, text="=", width=10, height=5, font='Helvetica 19 bold', bg="#3ED4E8",
                      command=lambda: clickequal())
    equal.grid(columnspan=2, rowspan=2, row=3, column=3)

    negative = tk.Button(root, text="+/-", width=4, height=2, font='Helvetica 20 bold', bg="#B9B9B9", command=lambda: pressnegative())
    negative.grid(row=4, column=0)

    clear = tk.Button(root, text='C', width=4, height=2, font='Helvetica 20 bold', bg="#B9B9B9",
                      command=lambda: clearpress())
    clear.grid(row=0, column=4)

    delete = tk.Button(root, text="<-", width=4, height=2, font='Helvetica 20 bold', bg="red",
                       command=lambda: deletecharacter())
    delete.grid(row=0, column=3)
    root.mainloop()


if __name__ == "__main__":
    driver()
