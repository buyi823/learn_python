#!/usr/bin/python
# dates are easily constructed and formatted

from datetime import date

now = date.today()
print('today:', now)

# dates support calendar arithmetic
birthday = date(1985, 7, 30)
age = now - birthday
print('days:', age.days)
print('age:', (age.days) / 365)
