from random import randint

def generate_warning():
    warnings = ['Ай-яй-яй','Я так не думаю','Что-то пошло не так','Произошла ошибка']
    return warnings[randint(0,len(warnings)-1)]