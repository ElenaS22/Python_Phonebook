import controller 

def storage(): #показать все контакты
    with open('data_file.txt', 'a+', encoding='utf-8') as data:
        return data
    
def add_contact(choice): #добавить контакт
    while choice == 1:
        with open('data_file.txt', 'a',  encoding='utf8') as data_file:
            print('Укажите данные для добавления')
            surname = input('Фамилия: ')
            name = input('Имя: ')
            tel_num = input('Телефон: ')
            data_file.writelines(f'{surname} {name} номер телефона {tel_num}\n')
            return choice
    
def finder(choice): #найти контакт
    with open('data_file.txt', 'r', encoding='utf-8') as data:
        users = data.read().splitlines()
        for values in users:
            if choice in values:
                print(f'\n {values} \n')
    return choice
   
def changer(contact_tochange): #изменить данные 
    changes = input('Введите новые данные: ')
    with open('data_file.txt', 'rt', encoding='utf-8') as data:
        users = data.read() 
        new_users = users.replace(contact_tochange, changes,1)
    with open('data_file.txt', 'wt', encoding='utf-8') as data:
        data.writelines(f'{new_users}\n')
    return contact_tochange

def delete_cont(contact_delete): #удалить контакт
    with open('data_file.txt', 'r+', encoding='utf-8') as data:
        users = data.read().splitlines()
    with open('data_file.txt', 'wt', encoding='utf-8') as data:    
        for values in users:
            if contact_delete not in values:
                data.writelines(f'{values}\n')
                print(f'удалено {contact_delete}')
        return contact_delete
