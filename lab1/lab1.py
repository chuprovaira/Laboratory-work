my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0])
print(my_list[2])
print(my_list[-1])
my_list[1] = 100

#2
for i in range(1, 11):
    print(i)
i = 10
while i >= 1:
 print(i)
 i -= 1

#3

num = int(input("Введите число: "))
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")
if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")


print("Введите число:")
n = int(input())
a = 0
for i in range(1, n + 1):
    print(i)

print("Введите первое число:")
n1 = int(input())
print("Введите второе число:")
n2 = int(input())
if n1 > n2:
    print("Большее число:", n1)
else:
    print("Большее число:", n2)
