# -*- coding: utf-8 -*-

hour, minutes, second = map(int,input().split())
elapsed = int(input())

min_to_sec = 60
hour_to_sec = 60 * min_to_sec
day_to_sec =  24 * hour_to_sec

start_time = hour * hour_to_sec + minutes * min_to_sec + second
end_time = start_time + elapsed

while True:
    if end_time > day_to_sec:
        end_time = end_time - day_to_sec
    else:
        break

result_hh = int(end_time / hour_to_sec)
result_mm = int(end_time % hour_to_sec / min_to_sec)
result_ss = int(end_time % hour_to_sec % min_to_sec)

print('{:d} {:d} {:d} '.format(result_hh, result_mm, result_ss))