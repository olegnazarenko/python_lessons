from random import randint, choice
from timeit import default_timer
from warnings_generator import generate_warning
import os


# функция выбора режима работы
def select_mode():

    mode = ''

    if os.path.exists(f'{name}_errors.txt'):

        print('''
    Режимы:
    1 - тренировка
    2 - работа над ошибками
    0 - выход
        ''')

        while mode not in {'0', '1', '2'}:
            print('Выберы режим:')
            mode = input()
            if mode not in {'0', '1', '2'}:
                print('Должно быть 0, 1 или 2')
    else:
        print('''
    Режимы:
    1 - тренировка
    0 - выход
        ''')
    
        while mode not in {'0', '1'}:
            print('Выберы режим:')
            mode = input()
            if mode not in {'0', '1'}:
                print('Должно быть 0, или 1')
    
    return mode

def remove_dublicate (file_name):

    uniques = [] #  уникальные примеры

    with open(file_name, 'r') as f, open(f'tmp_{file_name}', 'a') as f2:
        
        for line in f:
            if line not in uniques:
                uniques.append(line)
                f2.write(line)
    


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
    uniques_examples = []  # список уникальных примеров 
    example_number = 0  # номер примера

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

    for i in range(int(examples_quantity)):

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

       
            
        example = f'{number1} {sign} {number2}' 


        if example not in uniques_examples:
            uniques_examples.append(example)
            example_number +=1
            print(f'Пример {example_number}:')

        print('Сколько будет ',number1,sign,number2)
 
        start = default_timer()
        answer = input()
        while not answer.isdigit():
                    print('Должна быть цифра.')
                    answer = input()
        stop = default_timer()

        answer_time += round(stop - start)

        if correct_answer == answer:
            print('Правильно, молодец!')
            correct_answers += 1
        else:
            with open(f'{name}_errors.txt', 'a') as f:
                f.write(f'{number1} {sign} {number2} 3\n')
  
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


def fix_errors(name):
    with open(f'{name}_errors.txt','r') as f, open(f'tmp_{name}_errors.txt','a') as f2:

        for line in f:

            splited_line = line.split()
            number1, sign, number2, repeat = splited_line

            number1 = int(number1)
            number2 = int(number2)
            repeat = int(repeat)

            print(f'Сколько будет {number1} {sign} {number2}?')
            answer = int(input())

            if sign == '+':
                correct_answer = number1 + number2
            else:
                correct_answer = number1 - number2
            
            if correct_answer == answer:
                print('Правильно, молодец!')
                if int(repeat) > 1:
                    f2.write(f'{number1} {sign} {number2} {repeat-1}\n')
            else:
                print('Неправильно!')
                f2.write(f'{number1} {sign} {number2} {repeat}\n')
    
    os.remove(f'{name}_errors.txt')
    if os.path.getsize(f'tmp_{name}_errors.txt') > 0:
        os.rename(f'tmp_{name}_errors.txt', f'{name}_errors.txt')
    else:
        os.remove(f'tmp_{name}_errors.txt')
            
 


# основной блок программы
print('Привет! Меня зовут Роджер! А как тебя?')
name = input()
name = name.title()
print(f'Приятно познакомиться, {name}!')

remove_dublicate(f'{name}_errors.txt')

while True:
    mode = select_mode()
    if mode == '1':
        count()
    elif mode == '2':
        fix_errors(name)
    elif mode == '0':
        break
    else:
        pass




