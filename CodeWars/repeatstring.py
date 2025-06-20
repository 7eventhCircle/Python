def repeat_str(repeat, string):
    if any(c.isalpha() for c in string) or any(c.isdigit() for c in string):
        return string * repeat
    return ''
    

print(repeat_str(3, "Hey"))