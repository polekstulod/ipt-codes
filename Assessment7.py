
# ! I-comment muna ibang number bago i-run!
# * Number 1
# import tkinter as tk

# def sum_list(num):
#     num_list = []
#     for i in range(1, num + 1):
#         num_list+=[i]
#     return sum(num_list)

# def buttonClick():
#     num = int(entry1.get())
#     sum = sum_list(num)
#     tk.Label(master, text=f"The sum is 1 + .. + {str(num)} = {str(sum)}").grid(column=1, row=3)

# master = tk.Tk()
# master.geometry("300x100")

# tk.Label(master, text = "Enter Value of Integer: ").grid(column=0, row=1, padx=10, pady=10)
# entry1 = tk.Entry(master)
# entry1.grid(column=1, row=1)
# tk.Button(master, text="Validate", command=buttonClick).grid(column=1, row=4)

# master.mainloop()

# * Number 2
# import tkinter as tk

# def calculate(oprtr):
#     num1 = eval(operand1_entry.get())
#     num2 = eval(operand2_entry.get())
#     res = 0
#     sign.config(state=tk.NORMAL)
    
#     if oprtr == "+":
#         operator_sign.set("+")
#         res = num1+num2
#     elif oprtr == "-":
#         operator_sign.set("-")
#         res = num1-num2
#     elif oprtr == "*":
#         operator_sign.set("*")
#         res = num1*num2
#     elif oprtr == "/":
#         operator_sign.set("/")
#         res = num1/num2
#     elif oprtr == "^":
#         operator_sign.set("^")
#         res = num1**num2
#     elif oprtr == "%":
#         operator_sign.set("%")
#         res = num1%num2
        
#     sign.config(state=tk.DISABLED)
#     result.config(state=tk.NORMAL)
#     final_result.set(res)
#     result.config(state=tk.DISABLED)
    

# def clear_text():
#     operand1_entry.delete(0, 'end')
#     operand2_entry.delete(0, 'end')
#     sign.config(state=tk.NORMAL)
#     sign.delete(0, 'end')
#     sign.config(state=tk.DISABLED)
#     result.config(state=tk.NORMAL)
#     result.delete(0, 'end')
#     result.config(state=tk.DISABLED)
    
    
# master = tk.Tk()
# master.geometry("375x325")
# master.title("Simple Calculator")

# tk.Label(master, text="Simple Calculator").place(x=20, y=20)
# operators = tk.LabelFrame(master, text="Operators")
# operations = tk.LabelFrame(master, text="Operations")
# operand1_entry = tk.Entry(operations,width=10, justify=tk.CENTER)
# operand2_entry = tk.Entry(operations,width=10, justify=tk.CENTER)
# operator_sign = tk.StringVar()
# final_result = tk.StringVar()
# sign = tk.Entry(operations, width=5, textvariable=operator_sign, state=tk.DISABLED, justify=tk.CENTER)
# result = tk.Entry(operations, width=10, textvariable=final_result, state=tk.DISABLED, justify=tk.CENTER)

# operators.place(x=20, y=50)
# tk.Button(operators, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0, padx=5, pady=5)
# tk.Button(operators, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1, padx=5, pady=5)
# tk.Button(operators, text="*", width=5, command=lambda: calculate("*")).grid(row=1, column=0, padx=5, pady=5)
# tk.Button(operators, text="/", width=5, command=lambda: calculate("/")).grid(row=1, column=1, padx=5, pady=5)
# tk.Button(operators, text="\\", width=5).grid(row=2, column=0, padx=5, pady=5)
# tk.Button(operators, text="^", width=5, command=lambda: calculate("^")).grid(row=2, column=1, padx=5, pady=5)
# tk.Button(operators, text="Mod", width=5, command=lambda: calculate("%")).grid(row=3, column=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

# operations.place(x=180, y=50)
# tk.Label(operations, text="Operand 1: ").grid(row=0, column=0, padx=10, pady=10)
# operand1_entry.grid(row=0, column=1, padx=10, pady=10)
# sign.grid(row=1, column=1, padx=10, pady=10)
# tk.Label(operations, text="Operand 2: ").grid(row=2, column=0, padx=10, pady=10)
# operand2_entry.grid(row=2, column=1, padx=10, pady=10)
# tk.Label(operations, text="Result: ").grid(row=3, column=0, padx=10, pady=10)
# result.grid(row=3, column=1, padx=10, pady=10)

# tk.Button(master, text="Clear", width=10, command=clear_text).place(x=180, y=250)
# tk.Button(master, text="Exit", width=10, command=master.destroy).place(x=275, y=250)

# master.mainloop()


# * Number 3

import tkinter as tk

def calculate_total():
    subtotal_amount = 0
    
    bagel_amount = bagel.get()
    if bagel_amount == 1:
        subtotal_amount += 1.25
    elif bagel_amount == 2:
        subtotal_amount += 1.5
    
    if ck_btn1.get() == 1:
        subtotal_amount += .5
    if ck_btn2.get() == 1:
        subtotal_amount += .25
    if ck_btn3.get() == 1:
        subtotal_amount += .75
    if ck_btn4.get() == 1:
        subtotal_amount += .75
    if ck_btn5.get() == 1:
        subtotal_amount += .75
    
    coffee_amount = coffee.get()
    if coffee_amount == 2:
        subtotal_amount += 1.25
    elif coffee_amount == 3:
        subtotal_amount += 2
    elif coffee_amount == 4:
        subtotal_amount += 1.75
        
    tax_amount = round(subtotal_amount * 0.07, 2)
    total_amount = round(subtotal_amount - tax_amount, 2)
    
    subtotal_entry.config(state=tk.NORMAL)
    subtotal.set(subtotal_amount)
    subtotal_entry.config(state=tk.DISABLED)  
    
    tax_entry.config(state=tk.NORMAL)
    tax.set(tax_amount)
    tax_entry.config(state=tk.DISABLED)
    
    total_entry.config(state=tk.NORMAL)
    total.set(total_amount)
    total_entry.config(state=tk.DISABLED)

def clear_reset():
    subtotal_entry.config(state=tk.NORMAL)
    tax_entry.config(state=tk.NORMAL)
    total_entry.config(state=tk.NORMAL)
    subtotal_entry.delete(0, 'end')
    tax_entry.delete(0, 'end')
    total_entry.delete(0, 'end')
    subtotal_entry.config(state=tk.DISABLED)
    tax_entry.config(state=tk.DISABLED)
    total_entry.config(state=tk.DISABLED)
    bagel.set(None)
    ck_btn1.set(0)
    ck_btn2.set(0)
    ck_btn3.set(0)
    ck_btn4.set(0)
    ck_btn5.set(0)
    coffee.set(None)

master = tk.Tk()
master.geometry("450x450")
master.title("Bagel and Coffee Price Calculator")

tk.Label(master, text="Brandi's Bagel House", font=("Times New Roman", 20, "bold", "italic")).pack(pady=30)
frame1 = tk.Frame(master)
frame2 = tk.Frame(master)

frame1_a = tk.Frame(frame1)
frame1_a.pack(side=tk.LEFT,padx=10)
frame1_b = tk.Frame(frame1)
frame1_b.pack(fill='both',side=tk.RIGHT,padx=10)


label_frame1 = tk.LabelFrame(frame1_a, text="Pick a Bagel")
bagel = tk.IntVar()
tk.Radiobutton(label_frame1, text="White(1.25)", variable=bagel, value=1).pack(anchor=tk.W)
tk.Radiobutton(label_frame1, text="Whole Wheat(1.50)", variable=bagel, value=2).pack(anchor=tk.W)
label_frame2 = tk.LabelFrame(frame1_a, text="Pick Your Toppings")
ck_btn1 = tk.IntVar()
ck_btn2 = tk.IntVar()
ck_btn3 = tk.IntVar()
ck_btn4 = tk.IntVar()
ck_btn5 = tk.IntVar()
tk.Checkbutton(label_frame2, text="Cream Cheese(.50)", variable=ck_btn1).pack(anchor=tk.W)
tk.Checkbutton(label_frame2, text="Butter(.25)", variable=ck_btn2).pack(anchor=tk.W)
tk.Checkbutton(label_frame2, text="Blueberry Jam(.75)", variable=ck_btn3).pack(anchor=tk.W)
tk.Checkbutton(label_frame2, text="Raspberry Jam(.75)", variable=ck_btn4).pack(anchor=tk.W)
tk.Checkbutton(label_frame2, text="Peach Jelly(.75)", variable=ck_btn5).pack(anchor=tk.W)


label_frame3 = tk.LabelFrame(frame1_b, text="Want Coffee with that?")
coffee = tk.IntVar()
tk.Radiobutton(label_frame3, text="None", variable=coffee, value=1).pack(anchor=tk.W)
tk.Radiobutton(label_frame3, text="Regular Coffee(1.25)", variable=coffee, value=2).pack(anchor=tk.W)
tk.Radiobutton(label_frame3, text="Cappuccino(2.00)", variable=coffee, value=3).pack(anchor=tk.W)
tk.Radiobutton(label_frame3, text="Cafe au lait(1.75)", variable=coffee, value=4).pack(anchor=tk.W)
label_frame4 = tk.LabelFrame(frame1_b, text="Price")
tk.Label(label_frame4, text="Subtotal: ").grid(row=0, column=0,pady=3,sticky=tk.SE)
tk.Label(label_frame4, text="Tax: ").grid(row=1, column=0,sticky=tk.SE)
tk.Label(label_frame4, text="Total: ").grid(row=2, column=0,pady=3,sticky=tk.SE)
subtotal = tk.StringVar()
tax = tk.StringVar()
total = tk.StringVar()
subtotal_entry = tk.Entry(label_frame4, state=tk.DISABLED, width=10, textvariable=subtotal, justify=tk.CENTER)
tax_entry = tk.Entry(label_frame4, state=tk.DISABLED, width=10, textvariable=tax, justify=tk.CENTER)
total_entry = tk.Entry(label_frame4, state=tk.DISABLED, width=10, textvariable=total, justify=tk.CENTER)
subtotal_entry.grid(row=0, column=1,pady=3,sticky=tk.SE)
tax_entry.grid(row=1, column=1,sticky=tk.SE)
total_entry.grid(row=2, column=1,pady=3,sticky=tk.SE)


label_frame1.pack()
label_frame2.pack()
label_frame3.pack(fill='both')
label_frame4.pack(fill='both')


tk.Button(frame2, text="Calculate Total", width=15, command=lambda: calculate_total()).grid(row=0, column=0)
tk.Button(frame2, text="Reset Form", width=15, command=lambda: clear_reset()).grid(row=0, column=1, padx=20)
tk.Button(frame2, text="Exit", width=15, command=master.destroy).grid(row=0, column=2)

frame1.pack()
frame2.pack(pady=15)

master.mainloop()