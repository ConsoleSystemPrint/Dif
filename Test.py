import unittest
import sympy as sp
from Dif import differentiate_function

class TestDifferentiator(unittest.TestCase):

    def test_single_variable(self):
        result = differentiate_function('x**2', 'x')
        self.assertEqual(result[sp.symbols('x')], sp.sympify('2*x'))

    def test_multiple_variables(self):
        result = differentiate_function('x*y + sin(z)', 'x y z')
        self.assertEqual(result[sp.symbols('x')], sp.sympify('y'))
        self.assertEqual(result[sp.symbols('y')], sp.sympify('x'))
        self.assertEqual(result[sp.symbols('z')], sp.sympify('cos(z)'))

    def test_incorrect_function(self):
        result = differentiate_function('x**2 + sin(y', 'x y')
        self.assertEqual(result, "Ошибка: Некорректная запись функции.")

    def test_nonexistent_variable(self):
        result = differentiate_function('x**2', 'x y')
        self.assertEqual(result[sp.symbols('x')], sp.sympify('2*x'))
        self.assertIn(sp.symbols('y'), result)
        self.assertIsNone(result[sp.symbols('y')])

    def test_custom_functions(self):
        result = differentiate_function('tan(x)', 'x')
        self.assertEqual(result[sp.symbols('x')], sp.sympify('sec(x)**2'))

    def test_edge_cases(self):
        result = differentiate_function('log(x) + exp(y)', 'x y')
        self.assertEqual(result[sp.symbols('x')], sp.sympify('1/x'))
        self.assertEqual(result[sp.symbols('y')], sp.sympify('exp(y)'))

if __name__ == '__main__':
    unittest.main()