#There are following three methods those can do this behalf of us

# This approch reverse the string and then compare it with the
# the orignal string and check if both are equal
def isPalindromByReversingString(string):
    reverseString = ''
    for i in reversed(range(len(string))):
        reverseString = reverseString + string[i]
    if reverseString == string:
        return True
    else:
        return False


# Recursive approch to check if the ith and lenght - ith characters
# are equal
def isPalindromeByRecursion(string, lith, rith):
    if lith == rith:
        return True
    else:
        return string[lith] == string[rith] and isPalindromeByRecursion(string, lith+1, rith-1)

# Iterative approch to check if the ith and lenght - ith characters
# are equal
def isPalindromeByIteration(string, lith, rith):
    while not lith == rith:
        if not string[lith] == string[rith]:
            return False
        lith +=1
        rith -=1
    return True

if __name__ == '__main__':
    print(isPalindromByReversingString("abcdcba"))
    print(isPalindromeByRecursion("abcdcba", 0, 6))
    print(isPalindromeByIteration("abcdcba", 0, 6))