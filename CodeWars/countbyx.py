def count_by(x, n):
    result = []
    for i in range(1, n + 1):
        multiple = i * x
        result.append(multiple)
    return result


print(count_by(2, 5))
