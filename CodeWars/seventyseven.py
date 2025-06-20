import numpy as np

def generate_odd_magic_square(n):
    """Generates an n x n magic square for odd n using the Siamese method."""
    magic_square = np.zeros((n, n), dtype=int)
    num = 1
    i, j = 0, n // 2

    while num <= n ** 2:
        magic_square[i, j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i, new_j]:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square

# Generate the standard 7x7 magic square
base_square = generate_odd_magic_square(7)

# The default magic sum for 7x7 is 175
# We want to reduce it to 77, so we use an integer linear transformation:
# new_value = floor(original_value * scale + shift)
target_sum = 77
default_sum = base_square.sum(axis=1)[0]
scale = target_sum / default_sum

# Try multiple shift values to find one that preserves the magic properties
def find_valid_magic(square, scale, target_sum):
    for shift in range(-10, 11):  # test small shift values
        test_square = np.floor(square * scale + shift).astype(int)
        rows = test_square.sum(axis=1)
        cols = test_square.sum(axis=0)
        d1 = np.trace(test_square)
        d2 = np.trace(np.fliplr(test_square))
        if np.all(rows == target_sum) and np.all(cols == target_sum) and d1 == target_sum and d2 == target_sum:
            return test_square
    return None

# Try to find a working magic square
magic_7x7_77 = find_valid_magic(base_square, scale, target_sum)

if magic_7x7_77 is not None:
    print("Magic 7x7 Square with all sums = 77:")
    print(magic_7x7_77)
else:
    print("No exact magic square found with sum 77.")
