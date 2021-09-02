#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# By Blaine 2021-09-01 16:19
# 代码生成字典，列表

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# 显示前5个
for alien in aliens[:8]:
    print(alien)
print('......')

# 显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")