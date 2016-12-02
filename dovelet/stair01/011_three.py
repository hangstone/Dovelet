# -*- coding: utf-8 -*-

a = int(input())
b = int(input())

first = b%10
second = int(b/10%10)
third = int(b/100)

first_ans = a * first
second_ans = a * second
third_ans = a * third
forth_ans = a * b

print(first_ans)
print(second_ans)
print(third_ans)
print(forth_ans)