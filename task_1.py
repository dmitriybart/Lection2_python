colors = ['red', 'green', ' blue']
data = open ('file2a.txt', 'a') # а - доплоняет текст(не перезаписывает)
data.writelines(colors)
data.close()
exit()#остфновка кода