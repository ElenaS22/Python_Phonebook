import controller 
import shutil

def storage(): #показать все контакты
    with open('data_file.txt', 'r', encoding='utf-8') as data:
        return data
    with open('data_file.txt', 'r', encoding='utf-8') as data:
        return data
    
def add_contact(contact): #добавить контакт
    #return None
    with open('data_file.txt', 'a',  encoding='utf8') as data_file:
        data_file.write(f'{contact}\n')
    return contact
    #return None
    with open('data_file.txt', 'a',  encoding='utf8') as data_file:
        data_file.write(f'{contact}\n')
    return contact

def finder(contact): #найти контакт
    contact = input("Введите данные для поиска пользователя")
    with open('data_file.txt', 'r', encoding='utf-8') as data:
        match contact:
            case 1:
                name_finder = input("Введите ФИО пользователя: ")
                for values in data:
                    if data[values] == name_finder:
                        print(data[values])
            case 2:
                phone_finder = input("Введите ФИО пользователя: ")
                for values in data:
                    if data[values] == phone_finder:
                        print(data[values])

def changer(contact_change): #изменить данные
    return None
def delete_cont(contact): #удалить контакт
    return None

    return(contact_change)


def delete_cont(contact_delete): #удалить контакт
    contact_delete = input("Введите данные для удаление пользователя")
    shutil.rmtree(contact_delete)
     
    return contact_delete


# if __name__ == "__main__":
#     storage()