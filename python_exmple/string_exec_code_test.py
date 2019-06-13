 #!/usr/bin/python3
 # 将字符串作为代码执行

def exec_code(): 
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC) 
 
exec_code()
