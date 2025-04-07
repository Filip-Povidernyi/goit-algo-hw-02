from collections import deque


def palindrom(text: str) -> bool:

    text = text.lower()
    text = ''.join(filter(str.isalnum, text))
    deque_text = deque(text)

    if len(deque_text) == 0:
        return True
    elif len(deque_text) == 1:
        return True
    else:
        while len(deque_text) > 1:
            if deque_text.popleft() != deque_text.pop():
                return False
        return True


if __name__ == "__main__":
    text = "A man, a plan, a canal: Panama"
    print(palindrom(text))
