import sys

pref = input('Префиксная форма:')

stack = []

operators = set(['+', '-', '*', '/', '^'])

signs = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
if pref[0] in operators:

    print('Префиксная форма введена верно!')
else:

    print('Неверно введена префисная форма выражения!')
    sys.exit()

pref = pref[::-1]

for i in pref:

    if i in operators:

        a = stack.pop()
        b = stack.pop()
        res = a+b+i
        stack.append(res)

    else:
        stack.append(i)

print('Постфиксная форма:', *stack)