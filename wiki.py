import wikipedia 
wikipedia.set_lang('ru')
answer = input('Что вы хотите найти?\n')
t = wikipedia.page(answer)
print(t.content)