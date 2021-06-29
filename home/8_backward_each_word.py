# Дана строка. Необходимо найти все слова разделенные пробелом или пробелами,
# развернуть буквы в обратном порядке в каждом слове.

def backward_string_by_word(text: str) -> str:
    text_list = list(map(str, text.split(" ")))
    text_list_reversed = []
    for i in text_list:
        n = i[::-1]
        text_list_reversed.append(n)
    return str(' '.join(text_list_reversed))


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word('hello   world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
