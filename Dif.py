import tkinter as tk
import sympy as sp


def check_input_validity(function_str, variables_str):
    try:
        locals_dict = {}
        variables = sp.symbols(variables_str.replace(' ', '').split(','))
        parsed_function = sp.sympify(function_str, locals=locals_dict)

        if parsed_function.has(sp.zoo):
            return False, "Ошибка: Деление на 0 в функции", None

        return True, parsed_function, variables
    except sp.SympifyError as e:
        print(f"{e}")
        return False, f"Ошибка синтаксиса", None


def differentiate_function(function_str, variables_str):
    validity, parsed_function, variables = check_input_validity(function_str, variables_str)
    if not validity:
        return parsed_function

    derivatives = {}
    try:
        for var in variables:
            derivative = sp.diff(parsed_function, var)
            derivatives[var] = derivative
        return derivatives
    except Exception as e:
        print(f"{e}")
        return f"Ошибка при вычислении производной"


def differentiate_one_variable(function_str, diff_variable_str):
    validity, parsed_function, _ = check_input_validity(function_str, diff_variable_str)
    if not validity:
        return parsed_function

    diff_variable = sp.symbols(diff_variable_str)
    try:
        derivative = sp.diff(parsed_function, diff_variable)
        return derivative
    except Exception as e:
        print(f"{e}")
        return f"Ошибка при вычислении производной"


def calculate_derivative_at_point(function_str, diff_variable_str, point):
    validity, parsed_function, _ = check_input_validity(function_str, diff_variable_str)
    if not validity:
        return parsed_function

    diff_variable = sp.symbols(diff_variable_str)
    try:
        derivative = sp.diff(parsed_function, diff_variable)
        derivative_at_point = derivative.subs(diff_variable, point)
        return derivative_at_point
    except Exception as e:
        print(f"{e}")
        return f"Ошибка при вычислении производной"


def on_calculate():
    func_input = function_entry.get()
    var_input = variables_entry.get()
    point_input = point_entry.get()

    if ',' in var_input:
        result = differentiate_function(func_input, var_input)
        if isinstance(result, dict):
            result_str = "\n".join([f"∂/∂{v} = {d}" for v, d in result.items()])
        else:
            result_str = result
    else:
        if point_input:
            try:
                point = float(point_input)
                result = calculate_derivative_at_point(func_input, var_input, point)
                result_str = str(result)
            except ValueError:
                result_str = "Ошибка: Некорректное значение точки"
        else:
            result = differentiate_one_variable(func_input, var_input)
            result_str = str(result)

    result_text.set(result_str)


def on_substitute():
    func_input = function_entry.get()
    var_input = variables_entry.get()
    values_input = values_entry.get()

    validity, parsed_function, variables = check_input_validity(func_input, var_input)
    if not validity:
        result_text.set(parsed_function)
        return

    values = values_input.replace(' ', '').split(',')
    if len(values) != len(variables):
        result_text.set("Ошибка: Количество значений не соответствует количеству переменных")
        return

    subs_dict = {}
    for var, val in zip(variables, values):
        try:
            subs_dict[var] = float(val)
        except ValueError:
            print(f"{var}")
            result_text.set(f"Ошибка: Некорректное значение для переменной")
            return

    try:
        evaluated_function = parsed_function
        for var, val in subs_dict.items():
            evaluated_function = evaluated_function.subs(var, val)
        result_str = str(evaluated_function.evalf())
    except Exception as e:
        print(f"{e}")
        result_str = f"Ошибка при подстановке значений"

    result_text.set(result_str)

def on_button_click(value):
    widget_in_focus = app.focus_get()
    if widget_in_focus == function_entry:
        current = function_entry.get()
        function_entry.delete(0, tk.END)
        function_entry.insert(0, current + value)
    elif widget_in_focus == variables_entry:
        current = variables_entry.get()
        variables_entry.delete(0, tk.END)
        variables_entry.insert(0, current + value)
    elif widget_in_focus == point_entry:
        current = point_entry.get()
        point_entry.delete(0, tk.END)
        point_entry.insert(0, current + value)
    elif widget_in_focus == values_entry:
        current = values_entry.get()
        values_entry.delete(0, tk.END)
        values_entry.insert(0, current + value)

def remove_last_character():
    widget_in_focus = app.focus_get()
    if widget_in_focus == function_entry:
        current = function_entry.get()
        function_entry.delete(len(current) - 1)
    elif widget_in_focus == variables_entry:
        current = variables_entry.get()
        variables_entry.delete(len(current) - 1)
    elif widget_in_focus == point_entry:
        current = point_entry.get()
        point_entry.delete(len(current) - 1)
    elif widget_in_focus == values_entry:
        current = values_entry.get()
        values_entry.delete(len(current) - 1)

app = tk.Tk()
app.title("Калькулятор производных")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

function_label = tk.Label(frame, text="Функция:")
function_label.grid(row=0, column=0, pady=5)
function_entry = tk.Entry(frame, width=50)
function_entry.grid(row=0, column=1, pady=5, columnspan=4)

variables_label = tk.Label(frame, text="Переменные (через запятую):")
variables_label.grid(row=1, column=0, pady=5)
variables_entry = tk.Entry(frame, width=30)
variables_entry.grid(row=1, column=1, pady=5, columnspan=4)

point_label = tk.Label(frame, text="Точка:")
point_label.grid(row=2, column=0, pady=5)
point_entry = tk.Entry(frame, width=30)
point_entry.grid(row=2, column=1, pady=5, columnspan=4)

values_label = tk.Label(frame, text="Значения (через запятую):")
values_label.grid(row=3, column=0, pady=5)
values_entry = tk.Entry(frame, width=30)
values_entry.grid(row=3, column=1, pady=5, columnspan=4)

buttons_frame = tk.Frame(frame)
buttons_frame.grid(row=4, column=0, columnspan=5, pady=5)

buttons = [
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '^', ',',
    '0', '.', '(', ')', '=',
    'sin', 'cos', 'tan', 'log', 'exp',
    'sqrt', 'asin', 'acos', 'atan', 'sinh',
    'cosh', 'tanh',
    'x', 'y', 'z'
]

row_val = 0
col_val = 0
for button in buttons:
    tk.Button(buttons_frame, text=button, width=5, command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

left_arrow_btn = tk.Button(frame, text="←", command=remove_last_character)
left_arrow_btn.grid(row=5, column=0, columnspan=1, pady=5)

equal_btn = tk.Button(frame, text="Рассчитать производную", command=on_calculate)
equal_btn.grid(row=5, column=1, columnspan=2, pady=5)

substitute_btn = tk.Button(frame, text="Подставить значения", command=on_substitute)
substitute_btn.grid(row=5, column=3, columnspan=2, pady=5)

result_label = tk.Label(frame, text="Результат:")
result_label.grid(row=6, column=0, pady=5)
result_text = tk.StringVar()
result_entry = tk.Entry(frame, width=50, state='readonly', textvariable=result_text)
result_entry.grid(row=6, column=1, pady=5, columnspan=4)

app.mainloop()