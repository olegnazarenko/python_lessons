from random import randint, choice
from timeit import default_timer

print('Привет! Меня зовут Роджер! А как тебя?')
name = input()
name = name.capitalize()
print('Приятно познакомиться, '+name+'!')
print('''Давай проверим твои знания в математике.
Ты готов? (да или нет)''')
ready = input()
ready = ready.lower()

while ready not in {'да', 'нет'}:
    print('''Должно быть 'да' или 'нет'!
введи заново''')
    ready = input()
    ready = ready.lower()


if ready == 'да':
    examples_quantity = ''  # количество примеров
    maximum_answer = ''  # до скольки будем считать
    correct_answers = 0  # количество правильных ответов
    fails = 0  # количесво ошибок

    # зададим основные условия выполнения программы и проверим их
    while not examples_quantity.isdigit():
        print(name + ', сколько примеров ты готов решить?')
        examples_quantity = input()
        if examples_quantity.isdigit():
            while int(examples_quantity) < 1:
                print('Введи число больше 0')
                examples_quantity = input()
                while not examples_quantity.isdigit():
                    print('Должна быть цифра.')
                    examples_quantity = input()
        else:
            print('Должна быть цифра.')
    
    while not maximum_answer.isdigit():
        print(name + ', до скольки будем считать?')
        maximum_answer = input()
        if maximum_answer.isdigit():
            while int(maximum_answer) < 2:
                print('Введи число больше 1!')
                maximum_answer = input()
                while not maximum_answer.isdigit():
                    print('Должна быть цифра.')
                    maximum_answer = input()
        else:
            print('Должна быть цифра.')

    print('Хорошо тогда начинаем!')
    for question in range(int(examples_quantity)):

        number1 = randint(1,int(maximum_answer))
        number2 = randint(1,int(maximum_answer))
        sign = choice('+-')


        if sign == '-':
            while number1 < number2:
                number1 = randint(1,int(maximum_answer))
                number2 = randint(1,int(maximum_answer))
            correct_answer = number1 - number2
        if sign == '+':
            while number1 + number2 > int(maximum_answer):
                number1 = randint(1,int(maximum_answer))
                number2 = randint(1,int(maximum_answer))
            correct_answer = number1 + number2

        print('Пример ' + str(question+1) + ':')        
        print('Сколько будет ',number1,sign,number2)

        start = default_timer()
        answer = int(input())
        stop = default_timer()

        answer_time = stop - start

        if correct_answer == answer:
            print('Правильно, молодец!')
        else:
            print('Неправильно!')
            print(f'Правильный ответ: {correct_answer}')
else:
    print('''Передумал? Хорошо, может как нибудь в следующий раз...
''')
