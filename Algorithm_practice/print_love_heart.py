#!/usr/bin/python3

print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

#此处是根据心形曲线公式来的(x2+y2-1)3-x2y3=0
 #定义高  for x in range(-30, 30)])
 #定义宽  for y in range(30, -30, -1)]))
