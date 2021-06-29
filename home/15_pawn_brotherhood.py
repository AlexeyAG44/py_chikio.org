def safe_pawns(pawns: set) -> int:
    pawns_index = set()
    for p in sorted(pawns):
        print(sorted(pawns))
        print(p[1], ord(p[0]))
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        print(row)
        print(col)
        pawns_index.add((row, col))
    count = 0
    for row, col in pawns_index:
        is_safe = ((row - 1, col - 1) in pawns_index) or ((row - 1, col + 1) in pawns_index)
        if is_safe:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
