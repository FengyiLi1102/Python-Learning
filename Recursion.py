# A function can call itself, which is called the recursion.

def a(n):
    if n <= 0:
        print('d')
    else:
        print(n)
        a(n-1)
a(3)

def b(n):
    while n > 0:
        print(n)
        n -=1
    print('d')
b(3)