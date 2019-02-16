known = dict()


def ack(m, n):
    if m == 0:
        result = n + 1
        return result
    elif n == 0:
            return ack(m - 1, 1)
    elif m > 0 and n > 0:
            return ack(m - 1, ack(m, n - 1))


print(ack(12, 4))