from tkinter import *
from tkinter import messagebox, ttk
import calculatorbutton
from math import sqrt

def sqaure_root(value):
    try:
        txt.delete(0, END)
        txt.insert(END, str(sqrt(int(value))))
    except Exception as e:
        print(str(e))


def check_keepontop():
    if keepontop.get() == 1:
        window.attributes('-topmost', 1)
    else:
        window.attributes('-topmost', 0)

def change_theme():
    global theme
    if theme == "light":
        theme = "dark"
        background_col = "#000000"
        foreground_col = "#FFFFFF"
        btn_theme.config(text="Dark")
    else:
        background_col = "#FFFFFF"
        foreground_col = "#000000"
        theme = "light"
        btn_theme.config(text="Light")

    txt.config(bg=background_col, fg=foreground_col)
    get_numpad(bg=background_col, fg=foreground_col)

def open_settings():
    global btn_theme, keepontop
    win = Toplevel(window)
    win.title("Settings")
    win.attributes("-topmost", True)
    win.config(bg="#FFFFFF")

    lbl_title = Label(win, text="Settings", font=("Arial", 20), bg="#FFFFFF", fg="#000000")
    lbl_title.grid(row=0, column=0, sticky="w")

    frm_theme = Frame(win, bg="#FFFFFF")
    frm_theme.grid(row=1, column=0, pady=10, sticky="w")

    lbl_theme = Label(frm_theme, text="Theme:", font=("Arial", 14), bg="#FFFFFF", fg="#000000")
    lbl_theme.grid(row=0, column=0, sticky="w")

    btn_theme = ttk.Button(frm_theme, text="Light", command=change_theme)
    btn_theme.grid(row=0, column=1)

    chk_ontop = ttk.Checkbutton(win, text="Keep the calculator app on top", variable=keepontop, onvalue=1, offvalue=0, command=check_keepontop)
    chk_ontop.grid(row=2, column=0, pady=10, sticky="w")

    btn_close = ttk.Button(win, text="Close", command=lambda: win.destroy())
    btn_close.grid(row=3, column=0, sticky="w")

    win.mainloop()

def delete_sum():
    txt.delete(len(txt.get()) - 1, END)


def calculate_sum():
    try:
        sum_string = txt.get()
        operator_sign = ""
        value1 = 0
        value2 = 0
        for i in sum_string:
            if i == "+":
                operator_sign = "+"
            elif i == "-":
                operator_sign = "-"
            elif i == "*":
                operator_sign = "*"
            elif i == "/":
                operator_sign = "/"
            else:
                pass

        sum_list = sum_string.split(operator_sign)
        value1 = int(sum_list[0])
        value2 = int(sum_list[1])
        answer = 0
        if operator_sign == "+":
            answer = value1 + value2
        elif operator_sign == "-":
            answer = value1 - value2
        elif operator_sign == "*":
            answer = value1 * value2
        elif operator_sign == "/":
            answer = value1 / value2
        txt.delete(0, END)
        txt.insert(END, str(answer))
    except Exception as e:
        print(str(e))


def add_number(num):
    global sign_added
    if num == "+":
        if sign_added:
            calculate_sum()
        sign_added = True
    elif num == "-":
        if sign_added:
            calculate_sum()
        sign_added = True
    elif num == "*":
        if sign_added:
            calculate_sum()
        sign_added = True
    elif num == "/":
        if sign_added:
            calculate_sum()
        sign_added = True
    else:
        pass
    txt.insert(END, str(num))


def get_numpad(font=("Arial", 14), bg="#FFFFFF", fg="#000000"):
    frm_numpad = Frame(window, bg=bg)
    frm_numpad.grid(row=1, column=0, sticky="news")
    row = 3
    column = 0
    for i in range(1, 10):
        calculatorbutton.Button(frm_numpad, text=i, font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=add_number).grid(row=row, column=column, sticky="news")
        frm_numpad.rowconfigure(row, weight=1)
        frm_numpad.columnconfigure(column, weight=1)
        column += 1
        if column == 3:
            column = 0
            row -= 1

    calculatorbutton.Button(frm_numpad, text="0", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=add_number).grid(row=4, column=1, sticky="news")
    calculatorbutton.Button(frm_numpad, text="+", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=add_number).grid(row=1, column=3, sticky="news")
    calculatorbutton.Button(frm_numpad, text="-", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=add_number).grid(row=2, column=3, sticky="news")
    calculatorbutton.Button(frm_numpad, text="*", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=add_number).grid(row=3, column=3, sticky="news")
    calculatorbutton.Button(frm_numpad, text="/", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=add_number).grid(row=4, column=3, sticky="news")
    calculatorbutton.Button(frm_numpad, text="=", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=calculate_sum).grid(row=4, column=2, sticky="news")
    calculatorbutton.Button(frm_numpad, text="delete", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=delete_sum).grid(row=4, column=0, sticky="news")
    calculatorbutton.Button(frm_numpad, text="Square root", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=lambda: sqaure_root(txt.get())).grid(row=5, column=0, sticky="news")
    calculatorbutton.Button(frm_numpad, text="Clear", font=font, bg=bg, fg=fg, activebg="#F0F0F0", activefg="#000000", command=lambda: txt.delete(0, END)).grid(row=5, column=3, sticky="news")
    frm_numpad.rowconfigure(4, weight=1)
    frm_numpad.columnconfigure(1, weight=1)
    for i in range(1, 4):
        frm_numpad.rowconfigure(i, weight=1)

    frm_numpad.columnconfigure(3, weight=1)


def main():
    global window, txt, sign_added, theme, keepontop
    theme = "light"
    sign_added = False
    window = Tk()
    window.title("Calculator")
    window.config(bg="#FFFFFF")
    window.rowconfigure(1, weight=1)
    window.columnconfigure(0, weight=1)

    keepontop = IntVar(value=0)

    txt = Entry(window, bg="#FFFFFF", fg="#000000", font=("Arial", 28), borderwidth=0)
    txt.grid(row=0, column=0, sticky="news")

    menu = Menu(window)
    window.config(menu=menu)

    menu.add_command(label="Settings", command=open_settings)

    get_numpad(font=("Arial", 20))

    window.mainloop()