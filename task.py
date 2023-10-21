import os

# task1 
# with open ('result\\books.txt', 'r', encoding='utf-8') as f:
#     for i in range(3):
#         info = f.readline()
#         print(info)

new_file = open ("series.txt", 'w', encoding='utf-8')
new_file.write ("1. Последнее королевство 2015\n"
                "2. Рим 2005\n"
                "3. Версаль 2015\n"
                "4. Тюдоры 2007\n"
                "5. Террор 2018\n"
                "6. Человек в высоком замке 2015\n"
                "7. Белая королева 2013\n"
                "8. Братья по оружию 2001\n"
                "9. Медичи 2016\n"
                "10. Спартак 2010")

lines, words, symbols = 0, 0, 0
with open('series.txt', 'r', encoding='utf-8') as file:
    for i in file:
        lines += 1
        words += len([w for w in i.split() if w.isalpha()])
        symbols += len([s for s in i if s.isalnum()])
print(f'Количество строк в файле series.txt: {lines}\n'
      f'Количество слов: {words}\n'
      f'Число символов: {symbols}\n')

