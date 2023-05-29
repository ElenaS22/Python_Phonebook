import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input("Выберете нужную вам команду и введите соответствующую цифру: ")
        if answer == '1':
            data = model.storage()
            view.show_contacts(data)
        elif answer == '2':
            choice = int(input("Вы хотите добавить пользователя? Выберите 1, если да и 2, если нет "))
            res = model.add_contact(choice)
            if res: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '3':
            choice = input('Введите фамилию, имя или номер телефона искомого контакта: ')
            res = model.finder(choice)
        elif answer == '4':
            contact_tochange = input("Введите данные, которые хотите изменить: ")
            res = model.changer(contact_tochange)
            if res: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '5':
            contact_delete = input("Введите данные пользователя для поиска и удаления ")
            res = model.delete_cont(contact_delete)
            if res: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '6':
            view.ciao()
            break
        else:
            print()
            view.error()
        


# if __name__ == "__main__":
#     start()