import crud

LIST_FIELDS = [
    {'field': 'first_name', 'title': 'Поиск клиента по имени',
        'console_text': 'Введите имя клиента: '},
    {'field': 'last_name', 'title': 'Поиск клиента по фамилии',
     'console_text': 'Введите фамилию клиента: '},
    {'field': 'email', 'title': 'Поиск клиента по e-mail',
     'console_text': 'Введите email клиента: '},
    {'field': 'phone', 'title': 'Поиск клиента по номеру телефона',
     'console_text': 'Введите номер телефона клиента: '},
    {'field': 'all', 'title': 'Вывести весь список клиентов',
     'console_text': 'Нажмите Enter для продолжения: '},
]


def fill_db():
    clients = [
        {'first_name': 'Иван', 'last_name': 'Иванов', 'email': 'ivanov@mail.ru',
            'phones': '+7 (999) 999-99-99, +7 (995) 100-99-88'},
        {'first_name': 'Марина', 'last_name': 'Иванова', 'email': 'ivanova@mail.ru'},
        {'first_name': 'Кристина', 'last_name': 'Варкентин',
            'email': 'franki@gmail.com', 'phones': '+7 (999) 333-33-33'},
        {'first_name': 'Ольга', 'last_name': 'Васильева', 'email': 'vasya@gmail.com',
            'phones': '+7 (999) 444-44-44, +7 (995) 555-55-55'},
    ]

    for client in clients:
        crud.create_client(**client)

    print('Список клиентов успешно добавлен в БД')


def get_client_id(list_exec):

    print('Выберите дейтсвие')
    for key, value in enumerate(list_exec, start=1):
        print(f'{key}. {value}')
    choice = int(input('Введите номер действия: ')) - 1

    if choice < len(list_exec):
        if choice == 0:
            client_id = input('Введите код клиента: ')
        elif choice == 1:
            id = _get_field_id()
            value = input(LIST_FIELDS[id]['console_text']).strip()
            clients = _get_client(LIST_FIELDS[id]['field'], value)
            if clients:
                print('id', 'Имя', 'Фамилия')
                for client in clients:
                    print(*client[:3])
                client_id = int(input('Введите id клиента: '))
            else:
                print('Клиент не найден')
                return
    return client_id if client_id else 0


def add_client():
    first_name = input('Введите имя клиента: ')
    last_name = input('Введите фамилию клиента: ')
    email = input('Введите email клиента: ')
    phones = input(
        'Введите номер телефона клиента (можно несколько, разделенных запятыми или оставьте поле пустым)): ')
    new_id = crud.create_client(first_name, last_name, email, phones)
    if new_id:
        print(
            f'Клиент {first_name} {last_name} (код {new_id}) успешно добавлен в БД')


def change_client():
    client = {}
    list_exec = ['Ввести код клиента для изменения',
                 'Найти клиента через поиск']
    client_id = get_client_id(list_exec=list_exec)
    if client_id:
        client['client_id'] = client_id

    cur_client = _get_client('id', client_id)[0]
    cur_phones = ', '.join(_get_phones(client_id=client_id))

    first_name = input(
        f'Введите новое имя клиента (по-умолчанию: "{cur_client[1]}"): ')
    if first_name:
        client['first_name'] = first_name

    last_name = input(
        f'Введите новую фамилию клиента (по-умолчанию: "{cur_client[2]}"): ')
    if last_name:
        client['last_name'] = last_name

    email = input(
        f'Введите новый email клиента (по-умолчанию {cur_client[3]}): ')
    if email:
        client['email'] = email

    phones = input(
        f'Введите новый номер телефона клиента (по-умолчанию {cur_phones}): ')
    if phones:
        client['phones'] = phones

    _update_client(client)


def delete_client():
    list_exec = ['Ввести код клиента для удаления',
                 'Найти клиента через поиск для удаления']
    client_id = get_client_id(list_exec=list_exec)
    if client_id:
        crud.delete_phones(client_id=client_id)
        crud.delete_client(client_id)
        print('Клиент удален из БД')


def find_client():

    id = _get_field_id()
    value = input(LIST_FIELDS[id]['console_text']).strip()

    clients = _get_client(LIST_FIELDS[id]['field'], value)
    if clients:
        print('Найденные клиенты:')
        print('id', 'Имя', 'Фамилия', 'E-mail', 'Номера телефонов')
        for client in clients:
            phones = [phone[1] for phone in crud.get_phones(client[0])]
            print(*client, ', '.join(phones) if phones else '')
    else:
        print('Клиентов не найдено')


def _get_field_id():
    print('Выберите поле для поиска:')
    for key, field in enumerate(LIST_FIELDS, start=1):
        print(f'{key}. {field["title"]}')
    id = int(input('Введите номер поля: ')) - 1

    return id if id < len(LIST_FIELDS) else None


def _get_client(field_name: str, value: str):
    field = {
        field_name: value
    }
    if field_name not in ['all']:
        clients = crud.get_client(**field)
    else:
        clients = crud.get_client()

    return clients


def _update_client(client):
    if client['client_id']:
        crud.update_client(**client)
        print('Данные обновлены')


def add_phones():
    list_exec = ['Ввести код клиента для добавления телефона',
                 'Найти клиента через поиск для добавления телефона']
    client_id = get_client_id(list_exec=list_exec)
    if client_id:
        phones = input(
            'Введите номер телефона клиента (можно несколько, разделенных запятыми): ').strip()
        crud.create_phones(client_id, phones)
        print('Данные добавлены')


def _get_phones(client_id):
    phones = crud.get_phones(client_id)
    if phones:
        return [phone[1] for phone in phones]


def del_phones():
    list_exec = ['Ввести код клиента для удаления телефона',
                 'Найти клиента через поиск для удаления телефона']
    client_id = get_client_id(list_exec=list_exec)
    if client_id:
        phones = crud.get_phones(client_id)
        if phones:
            print('id', 'Номер телефона')
            for phone in phones:
                print(*phone)
            phone_id = int(input(
                'Введите id номера телефона (введите 0, чтобы удалить все номера клиента): '))
            if phone_id:
                crud.delete_phones(phone_id=phone_id)
            else:
                crud.delete_phones(client_id=client_id)
            print('Данные удалены')
