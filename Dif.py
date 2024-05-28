import sympy as sp

def check_input_validity(function_str, variables_str):
    try:
        locals_dict = {}
        variables = sp.symbols(variables_str)
        parsed_function = sp.sympify(function_str, locals=locals_dict)
        return True, parsed_function, variables
    except sp.SympifyError as e:
        return False, str(e), None

def differentiate_function(function_str, variables_str):
    validity, parsed_function, variables = check_input_validity(function_str, variables_str)
    if not validity:
        return f"Ошибка: Некорректная запись функции: {parsed_function}"

    derivatives = {}
    try:
        for var in variables:
            derivatives[var] = sp.diff(parsed_function, var)
        return derivatives
    except Exception as e:
        return f"Ошибка при вычислении производной: {e}"

def differentiate_one_variable(function_str, diff_variable_str):
    validity, parsed_function, _ = check_input_validity(function_str, diff_variable_str)
    if not validity:
        return f"Ошибка: Некорректная запись функции: {parsed_function}"

    diff_variable = sp.symbols(diff_variable_str)
    try:
        derivative = sp.diff(parsed_function, diff_variable)
        return derivative
    except Exception as e:
        return f"Ошибка при вычислении производной: {e}"

if __name__ == "__main__":
    while True:
        try:
            user_choice = int(input("Выберите тип дифференцирования:\n1. Частные производные по нескольким переменным\n2. Производная 1-й переменной\n3. Выйти\nВаш выбор: "))
            if user_choice == 1:
                func_input = input("Введите функцию нескольких переменных (например, 'x*y + sin(z)'): ")
                vars_input = input("Введите переменные через пробел (например, 'x y z'): ")
                result = differentiate_function(func_input, vars_input)
                print(result)
            elif user_choice == 2:
                func_input = input("Введите функцию одной переменной: ")
                var_input = input("Введите переменную для дифференцирования: ")
                result = differentiate_one_variable(func_input, var_input)
                print(result)
                while True:
                    eval_choice = input("Хотите вычислить значение производной в точке? (y/n): ")
                    if eval_choice.lower() == 'y':
                        value = float(input(f"Введите значение для переменной {var_input}: "))
                        diff_var = sp.symbols(var_input)
                        derivative_function = sp.lambdify(diff_var, result)
                        print(f"Значение производной в точке {value} равно {derivative_function(value)}")
                    elif eval_choice.lower() == 'n':
                        break
                    else:
                        print("Некорректный выбор, попробуйте снова.")
            elif user_choice == 3:
                print("Выход из программы.")
                break
            else:
                print("Некорректный выбор, попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка: {e}, попробуйте снова.")