def isPalindrome(s):
    for i in range(len(s)):
        if ord(s[i]) == ord(s[len(s)-i-1]):
            return True
        return False

print(isPalindrome(input()))