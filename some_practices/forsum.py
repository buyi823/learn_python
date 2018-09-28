# for sum
n = int(input('How many numbers to sum? '))
total = 0
for i in range(n):
    s = input('Enter number ' + str(i+1) + ': ')
    total = total + int(s)
print('The sum is ' + str(total))