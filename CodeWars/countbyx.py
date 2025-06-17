def count_by(x, n):
    result = []  # better name than "list"
    for i in range(1, n + 1):
        multiple = i * x
        result.append(multiple)
    print(result)
