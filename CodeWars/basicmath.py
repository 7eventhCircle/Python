def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
print(basic_op('+', 4, 7))   # ➜ 11
print(basic_op('-', 15, 18)) # ➜ -3
print(basic_op('*', 5, 5))   # ➜ 25
print(basic_op('/', 49, 7))  # ➜ 7.0