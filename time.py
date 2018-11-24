import time

print('unix: ', time.time())
print('\n')
print('tuple time: ', time.localtime(time.time()))
print('\n')
print('normal time: ', time.asctime(time.localtime(time.time())))
print('\n')
print('time', time.process_time())
print('\n\n\n\n')

import calendar

print('----------------------------------------')
print(calendar.month(2018, 11, w=5, l=2))

print('----------------------------------------')
print(calendar.calendar(2018))
