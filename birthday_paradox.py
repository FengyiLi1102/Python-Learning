import random as rad

def birthday_paradox(num_students):
    """
    Calculate the probability that find students with same birthday as me
    :param num_students: number of students
    :return: probability
    """

    birthday_all = []
    large_month_range = [1, 3, 5, 7, 8, 10, 12]
    my_birthday = [11, 2]

    for student in range(num_students):
        month = rad.randint(1, 12)
        if month == 2:
            day = rad.randint(1, 28)
        elif large_month_range.count(month) != 0:
            day = rad.randint(1, 31)
        else:
            day = rad.randint(1, 30)

        birthday_all.append([month, day])

    chance = birthday_all.count(my_birthday)
    print(birthday_all)

    return chance / num_students

