import tkinter as tk

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("não pode ne beh")
        expression = ""

calc = tk.Tk()
calc.title("calculadora")
calc.geometry("300x290") #corrigir

expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(calc)
input_frame.pack()

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bd=5, insertwidth=4, bg="pink", justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tk.Frame(calc)
btns_frame.pack()

tk.Button(btns_frame, text="7", command=lambda: btn_click(7), height=3, width=9).grid(row=1, column=0)
tk.Button(btns_frame, text="8", command=lambda: btn_click(8), height=3, width=9).grid(row=1, column=1)
tk.Button(btns_frame, text="9", command=lambda: btn_click(9), height=3, width=9).grid(row=1, column=2)
tk.Button(btns_frame, text="/", command=lambda: btn_click("/"), height=3, width=9, bg="purple").grid(row=1, column=3)
tk.Button(btns_frame, text="4", command=lambda: btn_click(4), height=3, width=9).grid(row=2, column=0)
tk.Button(btns_frame, text="5", command=lambda: btn_click(5), height=3, width=9).grid(row=2, column=1)
tk.Button(btns_frame, text="6", command=lambda: btn_click(6), height=3, width=9).grid(row=2, column=2)
tk.Button(btns_frame, text="x", command=lambda: btn_click("x"), height=3, width=9, bg="purple").grid(row=2, column=3)
tk.Button(btns_frame, text="1", command=lambda: btn_click(1), height=3, width=9).grid(row=3, column=0)
tk.Button(btns_frame, text="2", command=lambda: btn_click(2), height=3, width=9).grid(row=3, column=1)
tk.Button(btns_frame, text="3", command=lambda: btn_click(3), height=3, width=9).grid(row=3, column=2)
tk.Button(btns_frame, text="-", command=lambda: btn_click("-"), height=3, width=9, bg="purple").grid(row=3, column=3)
tk.Button(btns_frame, text="C", command=btn_clear, height=3, width=9).grid(row=4, column=0)
tk.Button(btns_frame, text="0", command=lambda: btn_click(0), height=3, width=9).grid(row=4, column=1)
tk.Button(btns_frame, text="=", command=btn_equal, height=3, width=9).grid(row=4, column=2)
tk.Button(btns_frame, text="+", command=lambda: btn_click("+"), height=3, width=9, bg="purple").grid(row=4, column=3)

calc.mainloop()
