def is_triangle(a, b, c):

    """
    Rules:
    a+b>c
    c-b<a
    """
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False

    return True

print(is_triangle(1,2,3))