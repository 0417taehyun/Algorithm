def reverseString(s: list) -> None:
    left, right = 0, len(s) - 1 # Two Point Appraoch
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == '__main__':
    strings = [
        ['h', 'e', 'l', 'l', 'o'],
        ['H', 'a', 'n', 'n', 'a', 'h']
    ]
    for string in strings:
        print(f"List '{string}' Result: {reverseString(string)}")