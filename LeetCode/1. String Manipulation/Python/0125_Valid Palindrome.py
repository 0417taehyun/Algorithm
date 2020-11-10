def isPalindrome(s: str) -> bool:
    strings = [ string.lower() for string in s if string.isalnum() ]
    return strings == strings[::-1]


if __name__ == '__main__':
    strings = [
        "A man, a plan, a canal: Panama",
        "Race a Car",
        ""
    ]
    for string in strings:
        print(f"String '{string}' Result: {isPalindrome(string)}")0