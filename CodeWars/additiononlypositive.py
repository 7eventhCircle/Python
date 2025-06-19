def positive_sum(arr):
    new_array = [x for x in arr if x > 0]
    if not new_array:
        return 0
    
    return sum(new_array)
    


print(positive_sum([3, -5, 6]))