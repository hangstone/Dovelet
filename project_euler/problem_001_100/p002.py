first = 1
second = 2
third = 3
Sum = 2

for i in range(4, 4000000):
    first = second
    second = third
    third = first + second

    if third % 2 == 0:
        Sum += third
    if Sum > 4000000:
        break

print (Sum)