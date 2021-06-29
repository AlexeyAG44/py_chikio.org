# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
# Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
# 0 < len(words) < 100


def checkio(words: str) -> bool:
    text_list = list(map(str, words.split(" ")))
    print(text_list)
    if 0 < len(text_list) < 100:
        count = 0
        for i in text_list:
            if not i.isdigit():
                count += 1
                if count >= 3:
                    break
            else:
                count = 0
        if count >= 3:
            return True
        else:
            return False
    else:
        return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
