from random import randint, choice
from timeit import default_timer
from warnings_generator import generate_warning


# функция выбора режима работы
def select_mode():
    print('''
   Режимы:
   1 - тренировка
   0 - выход
       ''')

    mode = ''
    while mode not in {'0', '1'}:
        print('Выберы режим:')
        mode = input()
        if mode not in {'0', '1'}:
            print('Должно быть 0, или 1')

    return mode

# функция возврата временных окончаний
def time_endings(seconds):
    if 10<seconds<20:
        return ''
    else:   
        digit = str(seconds)     
        last_digit = digit[-1]
        if last_digit == '1':
            return 'у'
        elif 1<int(last_digit)<5:
            return 'ы'
        else:
            return ''
        

# функция перевода секунд в секунды и минуты
def seconds_convert(time_in_seconds):
    if time_in_seconds < 60:
        time_spent = f'{time_in_seconds} секунд{time_endings(time_in_seconds)}'
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - (minutes * 60)

        if seconds == 0:
            time_spent = f'{minutes} минут{time_endings(minutes)}'
        else:
            time_spent = f'{minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(seconds)}'
    return time_spent  


# функция вывода примеров и их проверки
def count():
    print('Давай проверим твои знания в математике.')

    examples_quantity = ''  # количество примеров
    maximum_answer = ''  # до скольки будем считать
    correct_answers = 0  # количество правильных ответов
    fails = 0  # количесво ошибок
    answer_time = 0  # затраченое время на все ответы

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

        answer_time += round(stop - start)

        if correct_answer == answer:
            print('Правильно, молодец!')
            correct_answers += 1
        else:
            print(generate_warning())
            print(f'Правильный ответ: {correct_answer}')
            fails += 1
        
        print()
    if fails == 0:
        print('Молодец, ты ответил на все вопросы правильно!')
    else:
        print(f'Правильных ответов: {correct_answers}')
        print(f'Неправильных ответов: {fails}')    
    print(f'{seconds_convert(answer_time)}')
    

# основной блок программы
print('Привет! Меня зовут Роджер! А как тебя?')
name = input()
name = name.capitalize()
print(f'Приятно познакомиться, {name}!')



while True:
    mode = select_mode()
    if mode == '1':
        count()
    elif mode == '0':
        break
    else:
        pass




