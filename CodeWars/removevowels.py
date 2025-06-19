def disemvowel(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

print(disemvowel("your stupid"))