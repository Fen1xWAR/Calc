import ast
import math
import operator


class Calculator(object):
    # Список операций
    __operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }
    # Список функций
    __math_functions = {
        'exp' : math.exp,
        'sqrt': math.sqrt,
        'π': math.pi,
        'fact' : math.factorial,

    }

    @staticmethod
    def __evaluate(node):
        match type(node):
            case ast.Constant:  # Проверка на число
                return node.value
            case ast.BinOp:  # Проверка на бинарную операцию
                left = Calculator.__evaluate(node.left)
                right = Calculator.__evaluate(node.right)
                if type(node.op) in Calculator.__operations:
                    return Calculator.__operations[type(node.op)](left, right)
                else:
                    raise TypeError(f"Нет такой операции {type(node.op).__name__}")
            case ast.UnaryOp:  # Проверка на унарную операцию
                operand = Calculator.__evaluate(node.operand)
                if type(node.op) in Calculator.__operations:
                    return Calculator.__operations[type(node.op)](operand)
                else:
                    raise TypeError(f"Нет такой операции {type(node.op).__name__}")
            case ast.Name:  # Проверка имени операции
                print(node.id)
                if node.id in Calculator.__math_functions:
                    return Calculator.__math_functions[node.id]
                else:
                    raise TypeError(f"Нет такой функции {type(node.id).__name__}")
            case ast.Call:  # Проерка на вызов функции
                function = Calculator.__evaluate(node.func)
                node_arg = [Calculator.__evaluate(arg) for arg in node.args]
                print(function, node_arg)
                if callable(function):
                    return function(*node_arg)
                else:
                    raise TypeError(f"Ошибка вызова функции {type(function).__name__}")
            case _:
                raise Exception("Сюда не должно было дойти")

        # print(type(node))
        # # Операция над двумя частями (+ - / *)
        # if isinstance(node, ast.BinOp):
        #     left = Calculator.__evaluate(node.left)
        #     right = Calculator.__evaluate(node.right)
        #     if type(node.op) in Calculator.__operations:
        #         return Calculator.__operations[type(node.op)](left, right)
        #     else:
        #         raise TypeError(f"Нет такой операции {type(node.op).__name__}")
        # # Унарная операция (отрицание от числа)
        # elif isinstance(node, ast.UnaryOp):
        #     operand = Calculator.__evaluate(node.operand)
        #     if type(node.op) in Calculator.__operations:
        #         return Calculator.__operations[type(node.op)](operand)
        #     else:
        #         raise TypeError(f"Нет такой операции {type(node.op).__name__}")
        # # Случай для поиска функций
        # elif isinstance(node, ast.Name):
        #     print(node.id)
        #     if node.id in Calculator.__math_functions:
        #         return Calculator.__math_functions[node.id]
        #     else:
        #         raise TypeError(f"Нет такой функции {type(node.id).__name__}")
        # # Вызов функции - мат операции
        # elif isinstance(node, ast.Call):
        #     function = Calculator.__evaluate(node.func)
        #
        #     node_arg = [Calculator.__evaluate(arg) for arg in node.args]
        #     print(function, node_arg)
        #     if callable(function):
        #         return function(*node_arg)
        #     else:
        #         raise TypeError(f"Ошибка вызова функции {type(function).__name__}")
        # elif isinstance(node, ast.Num):
        #     return node.value
        # # Обработка для чисел
        # elif isinstance(node, ast.Constant):
        #     return node.value
        # else:
        #     raise Exception("Сюда не должно было дойти")

    @staticmethod
    def calculate_expression(expression):
        try:
            exp = ast.parse(expression, mode='eval')
            print(ast.dump(exp, exp))
            return Calculator.__evaluate(exp.body)
        except Exception as e:
            return "Ошибка " + str(e)


# Тут должен быть вызов из ui нашего калькулятора
#
# print(Calculator.calculate_expression(input()))
