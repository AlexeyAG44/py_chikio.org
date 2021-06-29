# У вас есть две даты в кортежах с тремя числами - год, месяц и день.
# Например, 19 апреля 1982 будет (1982, 4, 19).
# Вы должны найти разницу в днях между имеющимися датами.
# Например, между сегодня и вчера = 1 день.
# Разница между днями всегда будет положительной или нулем, не забывайте про абсолютное значение.

from datetime import date


def days_diff(a, b):
    d1 = date(*a)
    d2 = date(*b)
    return (abs(d2 - d1)).days


if __name__ == '__main__':
    print("Example:")
    print(days_diff((2014, 1, 1), (2014, 8, 27)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
