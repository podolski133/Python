from importlib.resources import path


# еще вариант: закрытие происходит автоматически
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# colors = ['red', 'green', 'blue'] # набор данных
# data = open('file.txt', 'w') # (путь к файлу,  и мод с которым работаем 'a' (есть еще r, w))
# data.writelines(colors) # производим запись // разделителей не будет
# data.close() # закрываем файл
## data.write('LINE 121\n')
## data.write('LINE 131\n')
## data.close()


path = 'file.txt'  # создаем путь к папке
data = open(path, 'r')  # затем откроем в режиме чтения
for line in data:  #  при помощи цыкла пробежимся по файлу
    print(line)  # и считаем все строки, и затем
data.close()  # разорвем связь

exit()