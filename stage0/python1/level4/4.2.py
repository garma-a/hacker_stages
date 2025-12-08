def isLargeEnough(s):
    return len(s) >= 8

def hasNumber(s):
    return any(char.isdigit() for char in s)

def hasSpecialChars(s):
    return any(not char.isalnum() for char in s)


def isStrongPassword(s):
    return isLargeEnough(s) and hasNumber(s) and hasSpecialChars(s)
