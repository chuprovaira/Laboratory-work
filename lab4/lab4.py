#1
from math import sqrt
number = int(input('Введите число:'))
print(sqrt(number))

from datetime import datetime
today = datetime.now()
print(today)

#2
import my_module

action1 = my_module.sum(1, 2)
action2 = my_module.squared(2, 4)

print(action1, action2)

#3
from package1 import *

x = sq_root(9) + square(2)
print(x)
print(greet('ggggh'))
print(describe_person('Ivan', 17))
