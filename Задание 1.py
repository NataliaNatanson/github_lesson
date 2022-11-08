statis = []
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = int(input('Введите шаг шифрования: '))
res =''
with open('ex.txt', 'r', encoding='ANSI') as f:
    for  i in f.read():
        i = i.lower()
        #i = i.isalpha()
        position = alf.find(i)
        new_position = position + key
        if i in alf:
            res += alf[new_position]


outW = open('shifr.txt', 'w', encoding='utf-8')
outW.write(res)
outW.close()

