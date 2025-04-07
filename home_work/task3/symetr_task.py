def symetric(string: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    opened = set(pairs.values())

    for ch in string:
        if ch in opened:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    if not stack:
        return True
    return False


if __name__ == "__main__":

    string = "( ){[ 1 ]( 1 + 3 )( ){ }}"
    print(symetric(string))
    string = "( 23 ( 2 - 3);"
    print(symetric(string))
    string = "( 11 }"
    print(symetric(string))
