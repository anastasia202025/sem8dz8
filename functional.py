def create(path):
    try:
        file = open(path ,'r')
    except IOError:
        print('Создан новый справочник ->phone_book.txt') 
        file = open(path,'w')   
    finally:
        file.close()   

def add_cont(file_name,stroka):
    data = open(file_name,'a') 
    data.write(stroka+"\n")
    data.close()  

def show_all(file_name):
    data = open(file_name,"r") 
    for line in data:
        print(line[:-1])
    data.close() 