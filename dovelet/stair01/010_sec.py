# -*- coding: utf-8 -*-

seconds = int(input())

minute_inSec = 60
hour_inSec = 60 * minute_inSec
day_inSec = 24 * hour_inSec

cur_day = int(seconds / day_inSec)
cur_hour = int(seconds % day_inSec / hour_inSec)
cur_min = int(seconds % day_inSec % hour_inSec / minute_inSec)
cur_sec = int(seconds % day_inSec % hour_inSec % minute_inSec)

print('{:d} {:d} {:d} {:d}'.format(cur_day, cur_hour, cur_min, cur_sec))