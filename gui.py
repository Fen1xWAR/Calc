
import tkinter as tk
from tkinter import ttk
from main import Calculator


evaluating_buffer = ""


def setup_ui(root):
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")
    root.title("Калькулятор")
    root.geometry("340x440")
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
    buttons_frame.grid(row=2, column=0, columnspan=4, sticky="s")

    # Корень
    sqrt_button = ttk.Button(buttons_frame, text="√", width=5, command=lambda text="sqrt(": add_char(text))
    sqrt_button.grid(row=0, column=0, padx=2, sticky="s")
    # ПиПИПИ
    pi_button = ttk.Button(buttons_frame, text='π', width=5, command=lambda text="π": add_char(text))
    pi_button.grid(row=0, column=1, padx=2, sticky="s")
    # EXP
    exp_button = ttk.Button(buttons_frame, text='e', width=5, command=lambda text="exp(": add_char(text))
    exp_button.grid(row=0, column=2, padx=2, sticky="s")
    # FAC
    fact_button = ttk.Button(buttons_frame, text="n!", width=5, command=lambda text="fact(": add_char(text))
    fact_button.grid(row=0, column=3, padx=2, sticky="s")

    # Долой все
    clear_all_button = ttk.Button(buttons_frame, text="AC", width=5, command=lambda: clear())
    clear_all_button.grid(row=1, column=0, pady=2, padx=2, sticky="nsew")
    # Скобки
    left_paren_button = ttk.Button(buttons_frame, text="(", width=5, command=lambda: add_char('('))
    left_paren_button.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
    right_paren_button = ttk.Button(buttons_frame, text=")", width=5, command=lambda: add_char(')'))
    right_paren_button.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

    # Делим
    divide_button = ttk.Button(buttons_frame, text="/", width=5, command=lambda: add_char('/'))
    divide_button.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

    # Долой последний символ
    clear_button = ttk.Button(buttons_frame, text="<=", width=5, command=lambda: clear_last_char())
    clear_button.grid(row=5, column=2, sticky="nsew", padx=2, pady=2)

    # РАВНОРАВНО
    button_evaluate = ttk.Button(buttons_frame, text="=", width=5, command=lambda: calculate())
    button_evaluate.grid(row=5, column=3, sticky="nsew", padx=2, pady=2)

    # Цифры
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
        ('0', 5, 0), ('.', 5, 1)
    ]

    for (text, row, col) in buttons:
        button = ttk.Button(buttons_frame, text=text, width=5, command=lambda t=text: add_char(t))
        button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

    # Настройка динамического изменения размера колонок и строк
    for i in range(6):
        buttons_frame.grid_rowconfigure(i, weight=1)
        buttons_frame.grid_columnconfigure(i, weight=1)

    style = ttk.Style()
    style.configure("TButton", padding=10, font=("Arial", 16))


def add_char(char):
    global evaluating_buffer
    text_field.config(state=tk.NORMAL)
    evaluating_buffer += char
    if text_field.get() == '0':
        text_field.delete(0, tk.END)
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
    data_to_calculate = evaluating_buffer.replace("^", "**")
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
