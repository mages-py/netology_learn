from db_utils import create_tables
import crud


def add_client():
    first_name = input('Введите имя клиента: ')
    last_name = input('Введите фамилию клиента: ')
    email = input('Введите email клиента: ')
    phones = input('Введите номер телефона клиента (можно несколько, разделенных запятыми или оставьте поле пустым)): ')
    crud.create_client(first_name, last_name, email, phones)


def find_client():
    list_fields = [
        {'field': 'first_name', 'title': 'Поиск клиента по имени', 'console_text': 'Введите имя клиента: '}, 
        {'field': 'last_name', 'title': 'Поиск клиента по фамилии', 'console_text': 'Введите фамилию клиента: '}, 
        {'field': 'email', 'title': 'Поиск клиента по e-mail', 'console_text': 'Введите email клиента: '}, 
        {'field': 'phone', 'title': 'Поиск клиента по номеру тедефона', 'console_text': 'Введите номер телефона клиента: '}, 
    ]
    
    print('Выберите поле для поиска:')
    for key, field in enumerate(list_fields, start=1):
        print(f'{key}. {field["title"]}')
    id = int(input('Введите номер поля: ')) - 1
    value = input(list_fields[id]['console_text']).strip()
    
    get_client(list_fields[id]['field'], value)
    
    
def get_client(field:str, value):
    if field == 'first_name':
        name = input('Введите имя клиента: ')
        client = crud.get_client(first_name=name)
    elif field == 'last_name':
        name = input('Введите фамилию клиента: ')
        client = crud.get_client(last_name=name)
    elif field == 'email':
        name = input('Введите email клиента: ')
        client = crud.get_client(email=name)
    elif field == 'phones':
        name = input('Введите номер телефона клиента: ')
        client = crud.get_client(phone=name)
    return client
                


EXEC_LIST = [
    {'func_name': create_tables, 'title': 'Создать структуру БД'},
    {'func_name': add_client,  'title': 'Добавить клиента в БД'},
    {'func_name': find_client,  'title': 'Поиск клиента в БД'},
]


def main():
    continue_execution = True
    while True:
        print('Выберите действие:')
        for key, func in enumerate(EXEC_LIST, start=1):
            print(f'{key}. {func["title"]}')
        id = int(input('Введите номер действия: ')) - 1
        if id < len(EXEC_LIST):
            EXEC_LIST[id]['func_name']()

        if input('Для продолжения нажмите Enter: ') == '':
            continue
        else:
            continue_execution = False

if __name__ == '__main__':
    main()
            