def custom_write(file_name , strings):
    ret = {}
    name = file_name
    file = open(name , 'a' , encoding= 'utf-8')
    for i in range(len(strings)):
        ret [(i+1 , file.tell())] = strings[i]
        file.write(strings[i])
        file.write('\n')
        if i == range(len(strings)):
         file.close()
    return ret



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
   print(elem)
#print(result)