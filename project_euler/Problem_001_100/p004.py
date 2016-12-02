def isPalindrome(value):
    IsPN = []

    while value / 10 > 1:
        IsPN.append(value % 10)
        value = value / 10
    IsPN.append(value)

    for i in range(0, len(IsPN)):
        if i == len(IsPN):
            ret = True
            break

        if IsPN[i] == IsPN[len(IsPN)- (i+1)]:
            ret = True
        else:
            ret = False
            break

    return ret

def findLargestPalindrome(a, b):
    ret = True
    threeDigit1 = a
    threeDigit2 = b
    answer_before = 0
    ansver_after = 0
    isFirstTime = True

    while True:
        pn = threeDigit1 * threeDigit2

        if isPalindrome(pn) == True:
            answer_after = threeDigit1 * threeDigit2
            if isFirstTime == True:
                answer_before = answer_after
                isFirstTime = False
            if answer_before < answer_after:
                answer_before = answer_after

        IsPN = []

        threeDigit2 = threeDigit2 - 1
        if threeDigit2 == 1:
            threeDigit2 = 999;
            threeDigit1 = threeDigit1 - 1

        if threeDigit1 == 1:
            break

    return answer_before

print (findLargestPalindrome(999, 999))

