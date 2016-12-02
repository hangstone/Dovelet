# -*- coding: utf-8 -*-

price = int(input())
change = 1000 - price
change100 = int(change / 100)
remainder100 = change - (change100 * 100)
change50 = int(remainder100 / 50)
remainder50 = remainder100 - (change50 * 50)
change10 = int(remainder50 / 10)

print('{:d} {:d} {:d}'.format(change100, change50, change10))