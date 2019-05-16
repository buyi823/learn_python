height = 1.75 # 1.75m
weight = 55 # 80.5kg
BMI=weight/(height*height) # BMI指数:体重除以身高的平方

if BMI < 18.5:
   print('too thin')
elif BMI > 18.5 and BMI < 25:
   print('nomal')
elif BMI > 25 and BMI < 28:
   print('fat')
else:
   print('too fat')
