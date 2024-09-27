
import tkinter as tk
from tkinter import ttk
from Calculator import Calculator


evaluating_buffer = ""


def setup_ui(root):
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    root.title("Калькулятор")
    root.geometry("340x460+450+150")
    root.resizable(False, False)

    # Создание текстового поля и лабеля
    special_button_frame = tk.Frame(root)
    special_button_frame.grid(row=1, column=0, columnspan=4,pady = 10)

    global expression_field, text_field
    expression_field = ttk.Label(special_button_frame, justify='right', text='', anchor='e',
                                 font=('Arial', 16))
    expression_field.grid(row=0, column=0, columnspan=4, padx=10, sticky='we')

    text_field = ttk.Entry(special_button_frame, width=20, justify="right", font=("Arial", 26))
    text_field.grid(row=1, column=0, columnspan=4, ipady=10, padx=10, pady=10, sticky="ew")
    text_field.insert(tk.END, "0")
    text_field.config(state=tk.DISABLED)

    create_buttons(root)


def create_buttons(root):
    buttons_frame = tk.Frame(root)
    buttons_frame.grid(row=2, column=0, columnspan=4, )

    # sin
    sin_button = ttk.Button(buttons_frame, text="sin", width=5, style="Accent.TButton",
                             command=lambda text="sin(": add_char(text))
    sin_button.grid(row=0, column=0, padx=2,pady=2, sticky="nsew")
    # cos
    cos_button = ttk.Button(buttons_frame, text='cos', width=5, style="Accent.TButton",
                           command=lambda text="cos(": add_char(text))
    cos_button.grid(row=0, column=1, padx=2,pady=2, sticky="nsew")
    # tan
    tan_button = ttk.Button(buttons_frame, text='tan', width=5, style="Accent.TButton",
                            command=lambda text="tan(": add_char(text))
    tan_button.grid(row=0, column=2, padx=2,pady=2, sticky="nsew")
    # пиии

    pi_button = ttk.Button(buttons_frame, text='π', width=5, style="Accent.TButton",
                           command=lambda text="π": add_char(text))
    pi_button.grid(row=0, column=3, padx=2,pady=2, sticky="nsew")


    # Корень
    sqrt_button = ttk.Button(buttons_frame, text="√n", width=5,style="Accent.TButton", command=lambda text="sqrt(": add_char(text))
    sqrt_button.grid(row=1, column=0, padx=2, sticky="nsew")
    # плов
    pow_button = ttk.Button(buttons_frame, text="n^", width=5, style="Accent.TButton",
                            command=lambda text="^": add_char(text))
    pow_button.grid(row=1, column=1, padx=2, sticky="nsew")

    # FAC
    fac_button = ttk.Button(buttons_frame, text="n!", width=5, style="Accent.TButton",
                            command=lambda text="fact": add_char(text))
    fac_button.grid(row=1, column=2, padx=2, sticky="nsew")

    # EXP
    exp_button = ttk.Button(buttons_frame, text='e', width=5,style="Accent.TButton", command=lambda text="exp(": add_char(text))
    exp_button.grid(row=1, column=3, padx=2, sticky="nsew")

    # Долой все
    clear_all_button = ttk.Button(buttons_frame, text="AC",style="Accent.TButton", width=5, command=lambda: clear())
    clear_all_button.grid(row=2, column=0, pady=2, padx=2, sticky="nsew")
    # Скобки
    left_paren_button = ttk.Button(buttons_frame, text="(", width=5,style="Accent.TButton", command=lambda: add_char('('))
    left_paren_button.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
    right_paren_button = ttk.Button(buttons_frame, text=")", width=5,style="Accent.TButton", command=lambda:  add_char(')' if evaluating_buffer.count("(")>0 else ''))
    right_paren_button.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

    # Делим
    divide_button = ttk.Button(buttons_frame, text="÷", width=5,style="Accent.TButton", command=lambda: add_char('/'))
    divide_button.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

    # Долой последний символ
    clear_button = ttk.Button(buttons_frame, text="⌫", width=5,style="Accent.TButton", command=lambda: clear_last_char())
    clear_button.grid(row=6, column=2, sticky="nsew", padx=2, pady=2)

    # РАВНОРАВНО
    button_evaluate = ttk.Button(buttons_frame, text="=", width=5,style="Accent.TButton", command=lambda: calculate())
    button_evaluate.grid(row=6, column=3, sticky="nsew", padx=2, pady=2)

    # пласплас
    plus_button = ttk.Button(buttons_frame, text="+", width=5, style="Accent.TButton", command=lambda: add_char('+'))
    plus_button.grid(row=5, column=3, sticky="nsew", padx=2, pady=2)
     # минус
    minus_button = ttk.Button(buttons_frame, text="-", width=5, style="Accent.TButton", command=lambda: add_char('-'))
    minus_button.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

    mult_button = ttk.Button(buttons_frame, text="*", width=5, style="Accent.TButton", command=lambda: add_char('*'))
    mult_button.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

    dot_button = ttk.Button(buttons_frame, text=".", width=5, style="Accent.TButton", command=lambda: add_char('.'))
    dot_button.grid(row=6, column=0, sticky="nsew", padx=2, pady=2)



    # Цифры
    buttons = [
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2),
         ('0', 6, 1)
    ]

    for (text, row, col) in buttons:
        button = ttk.Button(buttons_frame, text=text, width=5, command=lambda t=text: add_char(t))
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)


    style = ttk.Style()
    style.configure("TButton", padding=8, font=("Arial", 18))




def add_char(char):
    global evaluating_buffer
    text_field.config(state=tk.NORMAL)
    if text_field.get() == '0':
        text_field.delete(0, tk.END)
    if evaluating_buffer and evaluating_buffer[-1] in "+-*/^" and char in "+-*/^":

        evaluating_buffer = evaluating_buffer[:-1] + char
        text_field.delete(len(text_field.get()) - 1, tk.END)

    else:
        evaluating_buffer += char

    text_field.insert(tk.END, char)
    text_field.config(state='readonly')

def clear():
    global evaluating_buffer
    evaluating_buffer = ''
    expression_field.config(text='')
    update_display("0")


def clear_last_char():
    text_field.config(state=tk.NORMAL)
    current_text = text_field.get()
    text_field.delete(len(current_text) - 1, tk.END)
    if not text_field.get():
        update_display("0")
    else:
        text_field.config(state="readonly")


def update_display(text):
    text_field.config(state=tk.NORMAL)
    text_field.delete(0, tk.END)
    text_field.insert(tk.END, text)
    text_field.config(state="readonly")


def calculate():
    global evaluating_buffer
    count_bracket= evaluating_buffer.count("(") - evaluating_buffer.count(")")
    if count_bracket > 0:
        evaluating_buffer+=")"*count_bracket
    data_to_calculate = evaluating_buffer.replace("^", "**")
    data_to_calculate = data_to_calculate.replace("exp()", "exp(1)")

    expression_field.config(text=f"{data_to_calculate} =")
    result = Calculator.calculate_expression(data_to_calculate)

    if isinstance(result, (int, float)):
        update_display(result)
        evaluating_buffer = str(result)
    else:
        update_display("НЕВЕРНЫЙ ВВОД")



if __name__ == "__main__":
    root = tk.Tk()
    setup_ui(root)
    root.mainloop()
