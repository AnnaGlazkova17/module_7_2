def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8') # открываем/создаем файл для записи
    for i in range(len(strings)): # запись строк в файл
        # if i+1 == len(strings):       # 4-6 строки конструкция для записи без пустой строки в конце
        #     file.write(f'{strings[i]}')
        # else:
            print(f'{strings[i]}', file = file) # запись с помощью print
    file.close()
    result_1 = {} # создю пустой словарь
    file = open(file_name, 'r', encoding = 'utf-8') # открываем для чтения
    file.read() # читаем полностью
    end_text = file.tell() # запоминаем значение курсора в конце текста
    file.seek(0) # возвращает курсор в начало
    i = 1 # счетчик строк
    while file.tell() != end_text: # проверка на конец текста
        cursor = file.tell() # запоминает положение курсора в начале строки
        result_1[f'{i, cursor}'] = file.readline()[:-1]  # запись в список по ключа сторока и курсор, и строка без \n
        i = i + 1
    file.close()
    return result_1


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
