def greet(name):
return name
name_1=greet(input())
print('Hello',name_1,'!')
#вывод имени
def square(number):
return number**2
number_1=square(int((input())))
print('Квадрат числа равен:', number_1)
#возвращение квадрата числа
def max_of_two(x, y):
if x>y: return x
if y>x: return y
x_y=max_of_two(int(input()), int(input()))
print(x_y)
#озвращение максимального из двух чисел
def describe_person(name, age = 30):
return f"Name = {name}, age = {age}"
name = input()
age = input()
if age == '':
print(describe_person(name))
else:
print(describe_person(name, age))
import math
def is_prime(number):
if number<=0: return False
if number==2: return True
#единственное простое четное число
for i in range(2, int(math.sqrt(number))+1):
#перебираем числа от первого простого числа до корня number
if number>1 and number%i==0: return False
#число составное тк найден делитель
else: return True
#если делитель не найден, то число простое
z=is_prime(int(input()))
print(z)
