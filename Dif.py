import sympy as sp

def differentiate_function(function_str, variables_str):
    variables = sp.symbols(variables_str)
    try:
        math_functions = {
            'sin': sp.sin,
            'cos': sp.cos,
            'tan': sp.tan,
            'log': sp.log,
            'exp': sp.exp,
            'sqrt': sp.sqrt,
            'asin': sp.asin,
            'acos': sp.acos,
            'atan': sp.atan,
            'sinh': sp.sinh,
            'cosh': sp.cosh,
            'tanh': sp.tanh
        }

        function = sp.sympify(function_str, locals=math_functions)
    except sp.SympifyError:
        return "Ошибка: Некорректная запись функции."

    derivatives = {}
    try:
        for var in variables:
            derivatives[var] = sp.diff(function, var)
        return derivatives
    except Exception as e:
        return f"Ошибка при вычислении производной: {e}"

if __name__ == "__main__":
    func_input = input("Введите функцию нескольких переменных (например, 'x*y + sin(z)'): ")
    vars_input = input("Введите переменные через пробел (например, 'x y z'): ")
    result = differentiate_function(func_input, vars_input)
    print(result)    