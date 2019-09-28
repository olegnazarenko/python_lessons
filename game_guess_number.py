#Игра по угадыванию чисел
import random

print("Привет! Как тебя зовут?")
name = input()
name = name.title()

def guessNumber():

    print("Что ж,"+name+", я загадываю число от 1 до 20.")

    number = random.randint(1,20)
    counter = 0

    for counter in range(6):
        print("Попробуй угадать:")
        guess = int(input())

        if guess < number:
            print("Твоё число слишком маленькое!")

        if guess > number:
            print("Твоё число слишком большое!")

        if guess == number:
            break

    if guess == number:
        counter == str(counter + 1)
        print("Отлично, "+name+"! Ты справился за "+str(counter)+" попытки!")

    if guess != number:
        number = str(number)
        print("Увы. Я загадала число "+number)


play_game = 'да'
while play_game == "да":
    guessNumber()
    print("Повторим ещё? 'да' или 'нет'")
    play_game = input()
    while play_game not in {'да', 'нет'}:
        print("должно быть 'да' или 'нет'!")
        play_game = input()
if play_game == 'нет':
    print("Ну ладно, пока!")