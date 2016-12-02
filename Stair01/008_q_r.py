# -*- coding: utf-8 -*-
a,b = map(int,input().split())
quotient = int(a / b)
remainder = a % b
print('{:d} {:d}'.format(quotient, remainder))
