#!/usr/bin/python3
# filename: stopwatch
import time

print('按下回车开始计时，按下 Ctrl + C 停止计时。')
while True:
    try:
        input()
        starttime = time.time()
        # Python time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
        print('START')
        while True:
            print('计时： ', round(time.time() - starttime, 0), '秒', end="\r")
                # \r 默认将指针返回到最开始后输出（在原位置再次输出）
            time.sleep(1)
    except KeyboardInterrupt:
        print('END')
        endtime = time.time()
        print('总共时间为： ', round(endtime - starttime, 2), 'secs')
        break