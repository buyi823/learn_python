# timestable
for row in range(1,10):
    for col in range(1,10):
        prod = row * col
        if prod < 10:
            print(' ', end = '')
        print(str(row) + '*' + str(col) + '=' + str(row*col) + '  ', end = '')
    print()