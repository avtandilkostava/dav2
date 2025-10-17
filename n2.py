def foo(n):
    d = {}
    n = n.replace(" ", "")
    for i in n:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

n = input("enter a string -->")
print(foo(n))