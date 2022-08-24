def islower(c):
    n = ord(c)
    if n >= 97 and n <= 123:
        return True
    elif n < 97 or n > 123:
        return False
