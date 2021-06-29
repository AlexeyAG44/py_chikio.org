# Дана последовательность строк.
# Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
# В качестве шутки над праворукими роботами,
# вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова.
# Все строки даны в нижнем регистре.
# Предусловие: 0 < len(phrases) < 42

import re


def left_join(phrases: tuple) -> str:
    phrases_str = ",".join(phrases)
    result = re.sub(r'right', 'left', phrases_str)
    return result


if __name__ == '__main__':
    print('Example:')
    print(left_join(("bright aright", "ok")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
