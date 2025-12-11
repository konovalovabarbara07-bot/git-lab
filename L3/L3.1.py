# 1задание
from fileinput import filename


def read_all(filename):
    with open (filename, 'r', encoding='utf-8') as file:
        return file.read()
def read_lines(filename):
    with open (filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
filename='file.txt'
print('1-читать весь файл')
print('2-читать файл построчно')
choice = input('выберите')
if choice=='1':
    read_all(filename)
elif choice=='2':
    read_lines(filename)
else:
    print('ошибка')

# print('выбор чтения:1 - целиком, 2 - построчно')
# a=input('ввести число')
# if a=="1":
#     with open('file.txt','r', encoding='utf-8') as file:
#         content= file.read()
#         print(content)
# elif a=="2":
#     with open('file.txt','r', encoding='utf-8') as file:
#         for line in file:
#             print (line)
# else:
#     print('неверный тип')