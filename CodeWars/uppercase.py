def to_jaden_case(string):
    fixed_words = []
    
    for s in string.split():
        if s[0].isdigit():
            fixed_words.append(s)
        else:
            fixed_words.append(s.capitalize())
    return " ".join(fixed_words)


print(to_jaden_case("Hello 55 world"))