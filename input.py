
s = input("Знак (+,-,*,/): ")

if s in ('+','-','*','/'):
    x = float(input('Введите первое число: '))
    y = float(input('Введите второе число: '))
    if s == '+':
        res = print("%.2f" % (x + y))
    elif s == '-':
        res = print("%.2f" % (x - y))
    elif s == '*':
        res = print("%.2f" % (x * y))
    elif s == '/':
        if y != 0:
            res = print("%.2f" % (x / y))
        else:
            print("Деление на ноль!")
    else:
        print("Неверный знак операции!")
file = open('Тестовый файл.txt', 'a')
print (x, s, y, " = ", res, file=file)
file.close()