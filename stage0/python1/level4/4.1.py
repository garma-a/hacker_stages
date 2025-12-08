def reverse_string(s):
    return s[::-1]

def reverse_string2(s):
    return ''.join(reversed(s))

def reverse_string3(s):
    result = []
    for char in s:
        result.insert(0, char)
    return ''.join(result)
