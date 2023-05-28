# Дополнить телефонный справочник 
# возможностью изменения и удаления данных. 
# Пользователь также может ввести фамилию, 
# и Вы должны реализовать функционал для 
# изменения и удаления данных  
# 'a'- добавление ? Открывает файл и дописывает в него


# def interface():
#     print("1-добавление контакта \n 2-вывод всех \n 3-поиск по фамилии \n 4- выход")                
#     enter = int(input("Введите желаемый вариант"))
#     return enter



# def search (file_name,stroka):
#     a=0
#     data=open(file_name,'r')
#     for line in data:
# #         if sdef create(path):
#     try:
#         file = open(path ,'r')
#     except IOError:
#         print('Создан новый справочник ->phone_book.txt') 
#         file = open(path,'w')   
#     finally:
#         file.close()   

# def add_cont(file_name,stroka):
#     data = open(file_name,'a') 
#     data.write(stroka+"\n")
#     data.close()  

# def show_all(file_name):
#     data = open(file_name,"r") 
#     for line in data:
#         print(line[:-1])
#     data.close() troka in line:
#             print(line)
#             a=123
#             break
#         if a != 123:
#             print("нет такого контакта")
#         data.close    

# def del_name(file_name, del_name):
#     data = open(file_name,'r') #открытие для чтения данных
#     list_name=list()
#     for line in data:
#         if del_name in line:
#             print_name=line
#             continue
#         if line!="": list_name.append(line)
#         data.close()
#         list_name= list(filter(lambda x: x!="",list_name))
#         data = open(file_name,'w')
#         for item in list_name:
#             data.write(item)
#         data.close()
#         print(f"Контакт: {print_name}>> удален<<\n") 

# def change_name(file_name,ch_name):
#     data=open(file_name,'r') 
#     list_name = list() 
#     for line in data :
#         if ch_name in line:
#             new_name= input("Введите новое ФИО и номер телефона: ") 
#             list_name.append(new_name + "\n")
#             continue
#         list_name.append(line)
#     data.close()
#     list_name= list(filter(lambda x: x!="",list_name))
#     data = open(file_name,'w') #запись в текстовый файл старое стирается новое заносится
#     for item in list_name:
#         data.write(item)
#     data.close()  
#     print()               






# stroka1= 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = ['a','e','ё','и','й','у','ы','э','ю','я']
# phrases = stroka1.split()
# if len(phrases) < 2:
#     print('Количество фраз должно бытьбольше одной!')
# else:
#     countVowels = [] 

#     for i in phrases:
#         countVowels.append(len([x for x in i if x.lower()in vowels]))   
#     if len(set(countVowels)) ==1:
#         print('Парам пам -пам')
#     else:
#         print('Пам парам')    

# def print_operation_table(operation,num_rows=6,num_columns=6):
#     for i in range (num_rows):
#         for j in range(num_columns):
#             print(round(operation(i+1,j+1),3),end='\t')
#         print()
#     print()   

# print_operation_table(lambda x,y: x+y)
# print_operation_table(lambda x,y: x-y) 
# print_operation_table(lambda x,y: x*y)
# print_operation_table(lambda x,y: x/y)           
        




