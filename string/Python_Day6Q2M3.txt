def is_palindrome3(str):
    i = 0
    j = len(str)-1
    while i<j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome3('a'))