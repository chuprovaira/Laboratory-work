#1
def read(file_name, number):
    if number == 0:
        #чтение всего файла
        with open(file_name, 'r', encoding='utf-8') as file:
            read_file = file.read()
        print(read_file)
    elif number == 1:
        #чтение файла построчно
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                print(line)
file_name=input()
number=int(input())
read(file_name, number)

#2
def add(text, action):
 #1==добавить текст в новый файл, 2==добавить текст в существующий файл
    if action == 1:
        with open('user_input.txt', 'w') as file:
            file.write(text)
            return f'Запись прошла успешно'
    elif action == 2:
        with open('user_input.txt', 'a') as file:
            file.write(text)
            return f'Добавление прошло успешно'
text=input('Введите текст:')
action=int(input('Введите действие:'))
print(add(text, action))

#3
def read(file_name, number):
    try:
        if number == 0:
        # чтение всего файла
            with open(file_name, 'r', encoding='utf-8') as file:
                read_file = file.read()
            print(read_file)
        elif number == 1:
        # чтение файла построчно
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print('error')
file_name = str(input('Введите название файла:'))
number = int(input())
read(file_name, number)
