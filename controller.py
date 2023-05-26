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
            contact = input("Введите данные, которые нужно добавить: ")
            res = model.add_contact(contact)
            if res: 
                view.success(res)
            else: 
                view.not_success(res)
        elif answer == '3':
            contact = input("Введите данные для поиска: ")
            res = model.finder(contact)
            view.show_contacts(res)
        elif answer == '4':
            contact_change = input("Введите данные для изменения: ")
            res = model.finder(contact_change)
            view.show_contacts(res)

        elif answer == '5':
            contact_delete = input("Введите данные для удаления ")
            res = model.finder(contact_delete)
            view.show_contacts(res)
            pass 
        elif answer == '6':
            contact_delete = input("Выход")
            view.ciao()
        else:
            view.error()
        


# if __name__ == "__main__":
#     start()