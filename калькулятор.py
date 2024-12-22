import tkinter as tk

def get_values():
    num1 = int(number_1_entry.get())
    num2 = int(number_2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0,'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def minus():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mult():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


window = tk.Tk()

window.title('Calculator')
window.geometry('400x400')
window.resizable(False, False)

button_add = tk.Button(window, text = '+', width= 2, height= 2, command = add)
button_add.place(x = 100, y = 200)

button_minus = tk.Button(window, text = '-', width= 2, height= 2, command = minus)
button_minus.place(x = 140, y = 200)

button_mul = tk.Button(window, text = 'x', width= 2, height= 2, command = mult)
button_mul.place(x = 180, y = 200)

button_div = tk.Button(window, text = '/', width= 2, height= 2, comman = div)
button_div.place(x = 220, y = 200)

number_1_entry = tk.Entry(window, width = 25)
number_1_entry.place(x = 100, y = 100)
number1 = tk.Label(window, text = 'Введите первое число')
number1.place(x = 100, y = 75)

number_2_entry = tk.Entry(window, width = 25)
number_2_entry.place(x = 100, y = 160)
number2 = tk.Label(window, text = 'Введите второе число')
number2.place(x = 100, y = 135)

answer_entry = tk.Entry(window, width = 25)
answer_entry.place(x = 100, y = 300)
answer = tk.Label(window, text = 'Ответ')
answer.place(x = 100, y = 275)

window.mainloop()