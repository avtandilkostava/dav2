def foo(n):
    m = ""
    for i in range(len(n) - 1, -1, -1): 
        m += n[i]
    return m

n = input("enter a string --> ")
print(foo(n))
