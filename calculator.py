import tkinter as tk
from tkinter.ttk import *


calculation = ""

def display_cal(symbol):
    global calculation
    calculation += str(symbol)
    display_calculation.delete(1.0,"end")
    display_calculation.insert(1.0, calculation)

def evaluate_cal():
    global calculation
    try:
        calculation = str(eval(calculation))
        display_calculation.delete(1.0, "end")
        display_calculation.insert(1.0, calculation)
    except:
        clear()
        display_calculation.insert(1.0, "Error")

def press_button():
    pass

def clear():
    global calculation
    calculation = ""
    display_calculation.delete(1.0, "end")


root = tk.Tk()
root.geometry("261x260")
root.title("Calculator")
display_calculation = tk.Text(root, height=3, width=28, font=("Arial",13))
display_calculation.grid(columnspan=6)

# based on rows
btn_0 = tk.Button(root, text="0",width=11, font=("Arial" , 14), command= lambda : display_cal(0))
btn_0.grid(row = 6 ,column=1, columnspan=2)
btn_dot = tk.Button(root, text=".",width=5, font=("Arial" , 14), command= lambda : display_cal("."))
btn_dot.grid(row=6 , column=3)
btn_equal = tk.Button(root, text="=",width=5, font=("Arial" , 14), command= evaluate_cal)
btn_equal.grid(row=6 , column=4)
btn_1 = tk.Button(root, text="1",width=5, font=("Arial" , 14), command= lambda : display_cal(1))
btn_1.grid(row = 5 ,column=1)
btn_2 = tk.Button(root, text="2",width=5, font=("Arial" , 14),command= lambda : display_cal(2))
btn_2.grid(row = 5 ,column=2)
btn_3 = tk.Button(root, text="3",width=5, font=("Arial" , 14), command= lambda : display_cal(3))
btn_3.grid(row = 5 ,column=3)
btn_plus = tk.Button(root, text="+",width=5, font=("Arial" , 14), command= lambda : display_cal("+"))
btn_plus.grid(row=5 , column=4)
btn_4 = tk.Button(root, text="4",width=5, font=("Arial" , 14), command= lambda : display_cal(4))
btn_4.grid(row = 4 ,column=1)
btn_5 = tk.Button(root, text="5",width=5, font=("Arial" , 14), command= lambda : display_cal(5))
btn_5.grid(row = 4 ,column=2)
btn_6 = tk.Button(root, text="6",width=5, font=("Arial" , 14), command= lambda : display_cal(6))
btn_6.grid(row = 4 ,column=3)
btn_minus = tk.Button(root, text="-",width=5, font=("Arial" , 14), command= lambda : display_cal("-"))
btn_minus.grid(row=4 , column=4)
btn_7 = tk.Button(root, text="7",width=5, font=("Arial" , 14), command= lambda : display_cal(7))
btn_7.grid(row = 3 ,column=1)
btn_8 = tk.Button(root, text="8",width=5, font=("Arial" , 14), command= lambda : display_cal(8))
btn_8.grid(row = 3 ,column=2)
btn_9 = tk.Button(root, text="9",width=5, font=("Arial" , 14), command= lambda : display_cal(9))
btn_9.grid(row = 3 ,column=3)
btn_mul = tk.Button(root, text="x",width=5, font=("Arial" , 14), command= lambda : display_cal("*"))
btn_mul.grid(row=3 , column=4)
btn_clear = tk.Button(root, text="C",width=5, font=("Arial" , 14), command= clear)
btn_clear.grid(row=2 , column=1)
btn_negative = tk.Button(root, text="±",width=5, font=("Arial" , 14), command= lambda : display_cal("-"))
btn_negative.grid(row=2 , column=2)
btn_percent = tk.Button(root, text="%",width=5, font=("Arial" , 14), command= lambda : display_cal("%"))
btn_percent.grid(row=2 , column=3)
btn_div = tk.Button(root, text="÷",width=5, font=("Arial" , 14), command= lambda : display_cal("/"))
btn_div.grid(row=2 , column=4)

root.mainloop()


