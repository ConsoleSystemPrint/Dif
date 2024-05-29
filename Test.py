import unittest
from Dif import *

class TestMathOperations(unittest.TestCase):

    def test_check_input_validity_valid(self):
        valid, parsed_function, variables = check_input_validity("x**2 + y**2", "x, y")
        self.assertTrue(valid)
        self.assertEqual(str(parsed_function), "x**2 + y**2")
        self.assertEqual(len(variables), 2)

    def test_check_input_validity_invalid_syntax(self):
        valid, parsed_function, variables = check_input_validity("x**2 + y**2 *", "x, y")
        self.assertFalse(valid)
        self.assertEqual(parsed_function, "Ошибка синтаксиса")

    def test_check_input_validity_div_zero(self):
        valid, parsed_function, variables = check_input_validity("1/x", "x")
        self.assertTrue(valid)
        self.assertIn(sp.zoo, parsed_function.atoms())

    def test_differentiate_function(self):
        derivatives = differentiate_function("x**2 + y**2", "x, y")
        self.assertEqual(str(derivatives[sp.symbols('x')]), "2*x")
        self.assertEqual(str(derivatives[sp.symbols('y')]), "2*y")

    def test_differentiate_function_invalid(self):
        result = differentiate_function("x**2 + y**2*", "x, y")
        self.assertEqual(result, "Ошибка синтаксиса")

    def test_differentiate_one_variable(self):
        derivative = differentiate_one_variable("x**2", "x")
        self.assertEqual(str(derivative), "2*x")

    def test_differentiate_one_variable_invalid(self):
        result = differentiate_one_variable("x**2 *", "x")
        self.assertEqual(result, "Ошибка синтаксиса")

    def test_calculate_derivative_at_point(self):
        result = calculate_derivative_at_point("x**2", "x", 3)
        self.assertEqual(str(result), "6.00000000000000")

    def test_calculate_derivative_at_point_invalid(self):
        result = calculate_derivative_at_point("x**2*", "x", 3)
        self.assertEqual(result, "Ошибка синтаксиса")

    def test_on_substitute(self):
        global function_entry, variables_entry, values_entry, result_text
        class MockEntry:
            def __init__(self, text):
                self._text = text
            def get(self):
                return self._text

        class MockStringVar:
            def __init__(self):
                self._text = ""
            def set(self, text):
                self._text = text
            def get(self):
                return self._text

        function_entry = MockEntry("x**2 + y**2")
        variables_entry = MockEntry("x, y")
        values_entry = MockEntry("3, 4")
        result_text = MockStringVar()

        on_substitute()
        self.assertEqual(result_text.get(), "25.0")

    def test_on_substitute_invalid(self):
        global function_entry, variables_entry, values_entry, result_text
        class MockEntry:
            def __init__(self, text):
                self._text = text
            def get(self):
                return self._text

        class MockStringVar:
            def __init__(self):
                self._text = ""
            def set(self, text):
                self._text = text
            def get(self):
                return self._text

        function_entry = MockEntry("x**2 + y**2")
        variables_entry = MockEntry("x, y")
        values_entry = MockEntry("3, a")
        result_text = MockStringVar()

        on_substitute()
        self.assertEqual(result_text.get(), "Ошибка: Некорректное значение для переменной")

if __name__ == '__main__':
    unittest.main()