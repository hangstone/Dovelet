import math

ret = False
value = 600851475143
temp = int(math.sqrt(value))
gg = 0

for i in range(temp, 0, -1):
    if value % i == 0:
        gg = i

        for j in range(2, gg):
            if gg % j == 0:
                ret = False
                break
            ret = True

        if ret == True:
            break

print (gg)