# Вам дана строка и два маркера (начальный и конечный).
# Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
# Начальный и конечный маркеры всегда разные
# Если нет начального маркера, то началом считать начало строки
# Если нет конечного маркера, то концом считать конец строки
# Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
# Если конечный маркер стоит перед начальным, то вернуть пустую строку
# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
# Output: Строка.
# Предусловия: не может быть более одного маркера одного типа

def between_markers(text: str, begin: str, end: str) -> str:
    a = text.find(begin)
    b = text.find(end)
    if a == -1 and b == -1:
        res = text
    elif a == -1:
        res = text[0:b]
    elif b == -1:
        res = text[a + len(begin):]
    else:
        res = text[a + len(begin):b]
    return res


if __name__ == '__main__':
    print('Example:')
    print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
