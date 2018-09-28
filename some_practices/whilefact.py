# while factorial

n = int(input('Enter a integer >= 0: '))
fact = 1
i = 2
while i <= n:
    fact = fact * i
    i = i + 1
print(str(n) + ' factorial is ' + str(fact))