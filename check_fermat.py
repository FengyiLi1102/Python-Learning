import math

def check_fermat(a, b, c, n):
    if n <= 2 or type(a and b and c and n) is not int or a * b * c < 0:
        raise ValueError

    oo = 1
    for b in range(1, b):
        for a in range(1, a):
            for n in range(2, n):
                c = math.log((a**n + b**n), n)
                if type(c) is int:
                    print('Holy smokes, Fermat was wrong!')
                    oo = 2
                    break

    if oo == 1:
        print('No, that doesn\'t work')


def check_fermat_input():
    a = int(input('Please type your a: '))
    b = int(input('Please type your b: '))
    c = int(input('Please type your c: '))
    n = int(input('Please type your n: '))
    check_fermat(a, b, c, n)

check_fermat_input()