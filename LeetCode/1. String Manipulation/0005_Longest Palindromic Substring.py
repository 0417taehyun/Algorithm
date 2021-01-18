def longestPalindrome(s: str) -> str:
    word   = ''
    length = 0

    for idx in range(len(s)):
        # even
        left, right = idx, idx
        while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
            if (right - left + 1) > length:
                word   = s[left:right + 1]
                length = right - left + 1
            left  -= 1
            right += 1

        # odd
        left, right = idx, idx + 1
        while (left >= 0) and (right <= len(s) - 1) and (s[left] == s[right]):
            if (right - left + 1) > length:
                word   = s[left:right + 1]
                length = right - left + 1
            left  -= 1
            right += 1 
    
    return word

    


if __name__ == "__main__":
    words = ['babad', 'cbbd', 'a', 'ac']
    for word in words:
        print(longestPalindrome(word))