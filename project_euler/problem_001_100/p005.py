def canBeDivisible(number, natualNumber):
    if (number % natualNumber == 0):
        return True
    else:
        return False

def calculate():
    a = 2520123
    while True:
        isFound = True
        for i in range(2, 21):
            if (0 != a%i):
                isFound = False
                break
        if isFound == False:
            a = a + 1
        else:
            break

    print (a)

calculate()

