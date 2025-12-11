# 3задание
# print('выбор чтения:1 - целиком, 2 - построчно')
# a=input('ввести число')
# try:
#     with open('file.txt','r',encoding='utf-8') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print('Файл не найден')
# else:
#     if a == "1":
#         with open('file.txt', 'r', encoding='utf-8') as file:
#             content = file.read()
#             print(content)
#     elif a == "2":
#         with open('file.txt', 'r', encoding='utf-8') as file:
#             for line in file:
#                 print(line)
#     else:
#         print('неверный тип')

def read_all(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        return ('файл не найден')
def read_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                return (line)
    except FileNotFoundError:
        print('файл не найден')
print('1-читать весь файл')
print('2-читать файл построчно')
choice = input('выберите')
filename=input('введите имя файла:')
if choice=='1':
    read_all(filename)
elif choice=='2':
    read_lines(filename)
else:
    print('ошибка')
