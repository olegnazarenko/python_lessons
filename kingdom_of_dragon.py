# Игра "Царство драконов"
import random, time


def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры.
    В одной из них - дружелюбный дракон,
    который готов поделиться с вами своими сокровищами.
    Во второй - жадный и голодный дракон, который мигом вас съест.
    
    ''')

def chooseCave():
    cave = ''
    while cave != 1 and cave != 2:
        print("В какую пещеру вы войдёте? (нажмите клавишу 1 или 2)")
        cave = int(input())

    return cave

def checkCave(choosenCave):
    print("Вы приближаетесь к пещере...")
    time.sleep(3)
    print("Её темнота заставляет вас дрожать от страха...")
    time.sleep(3)
    print("Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...")
    time.sleep(3)

    friendlyCave = random.randint(1,2)
    if (choosenCave == friendlyCave):
        print("... делится с вами своими сокровищами!")
    else:
        print("... моментально вас съедает!")

playAgain = 'да'
while playAgain == 'да':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Попытаeте удачу ещё раз? (да или нет)")
    playAgain = input()