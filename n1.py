def foo(n):
    s = set(n.replace(" ", ""))
    if len(s) == len(n.replace(" ", "")):
        return True
    return False

n = input("enter a string --> ")
print(foo(n))