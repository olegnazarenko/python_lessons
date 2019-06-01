#! /usr/bin/env python
# -*- coding: utf-8 -*-

print ('Ваше имя?')
name = input ()
print('Ваш возраст?')
age = int(input())
if age>=18 and age<=60:
    myfile = open('users.txt', 'w')
    print('Имя: ', name, ', возраст: ', age, file=myfile)
    myfile.close()
    print('Спасибо!')
elif age<18:
    print('Вы слишком молоды')
elif age>60:
    print('Пока')