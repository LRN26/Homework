def is_palindrome(s: str):
    """a function checks whether a string is a palindrome or not."""

    s = s.lower()
    i = 0
    j = len(s)-1
    while i<j:
        if s[i] != s[j]:
            return 'string is not a palindrome'
        i += 1
        j -= 1
    return 'string is a palindrome'

print(is_palindrome('Madam'))
