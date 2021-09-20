import random
from sympy.abc import x
from sympy import *
c1 = random.randrange(10)
c2 = random.randrange(10)
c3 = random.randrange(10)
c4 = random.randrange(10)
c5 = random.randrange(10)
c6 = random.randrange(10)
c7 = random.randrange(10)
c8 = random.randrange(10)
c9 = random.randrange(10)
c10 = random.randrange(10)
dividend = c1 * x ** 5 + c2 * x ** 4 + c3 * x ** 3 + c4 * x ** 2 + c5 * x + c6
divider = c7 * x ** 2 + c8 * x ** 1 + c9
rem,q = div (dividend , divider)
print('Делимое равно:', (dividend))
print('Делитель равен:' , (divider))
print('Частное равно:', rem)
print('Остаток равен:', q)



