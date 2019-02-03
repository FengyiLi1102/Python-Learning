def gcd_slow(a, b):
    a_factor = []
    b_factor = []
    for i in range(1, a + 1):
        if a % i == 0:
            a_factor.append(i)

    for i in range(1, b + 1):
        if b % i == 0:
            b_factor.append(i)

    a_factor.sort(reverse=True)
    b_factor.sort(reverse=True)

    for i in range(len(a_factor)):
        for k in range(len(b_factor)):
            if a_factor[i] == b_factor[k]:
                return a_factor[i]
            elif a_factor[i] > b_factor[k]:
                break


def size(a, b):
    if a < b:
        c = a
        a = b
        b = c


def gcd_fast(a , b):
    r = a % b
    if r != 0:
        return gcd_fast(b, r)
    else:
        return b

print(gcd_fast(123141231231, 232314))