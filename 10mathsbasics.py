def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2

print(basic_op('/', 9.5, 8))

#определяем оператор и подставляем аргументы в соотв. операцию