# colors = ['red', 'green', ' blue']
# data = open('C:/Users/Dmitriy/Desktop/Разработчик ГБ/8Знакомство с языком Python/Lections2.0/Lesson_2/file2a.txt', 'a') # а - доплоняет текст(не перезаписывает)
# data.writelines(colors)
# data.close()
# exit()#остановка кода

with open ('file2a.txt', 'w') as data: # w - переписывает данные
    data.write('line1\n')
    data.write('line2\n')