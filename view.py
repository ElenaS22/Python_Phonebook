import model
def greetings():
   return print('Добрый день, уважаемый пользователь!\n')

def menu():
   print('Далее Вам будет предложен выбор категории справочника: \n\n'
         '1 - Показать все контакты\n'
         '2 - Добавить контакт\n'
         '3 - Найти контакт\n'
         '4 - Изменить данные контакта\n'
         '5 - Удалить данные контакта\n'
         '6 - Выход\n')
   
def show_contacts(data): # показать все контакты
   with open('data_file.txt', 'r', encoding='utf-8') as data:
      data_contains = data.read()
      print(data_contains)
    

def success(res): # показать найденный контакт
   if res:
      print("Операция прошла успешно!\n")
      

def not_success(res): # показать , что контакт не найден/отсутствует
   if not res:
      print("Операция провалена!\n")

def ciao():
    print()
    print("До свидания!\n")

def error():
   return print("Упс, что-то пошло не так! \n")


        
   


   

# if __name__ == "__main__":
#    greetings()
#    menu()
#    show_contacts()

