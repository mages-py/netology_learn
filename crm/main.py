from db_utils import create_tables
from db_client import add_client, find_client, add_phones, del_phones, fill_db, delete_client, change_client


EXEC_LIST = [
    {'func_name': create_tables, 'title': 'Создание структуры БД'},
    {'func_name': fill_db, 'title': 'Заполнение базы данными'},
    {'func_name': add_client,  'title': 'Создание клиента'},
    {'func_name': find_client,  'title': 'Поиск клиента'},
    {'func_name': change_client,  'title': 'Изменение данных клиента'},
    {'func_name': delete_client,  'title': 'Удаление клиента'},
    {'func_name': add_phones,  'title': 'Добавление телефонов для клиента'},
    {'func_name': del_phones,  'title': 'Удаление телефонов для клиента'},
]


def main():
    continue_execution = True
    while continue_execution:
        print('Выберите действие:')
        for key, func in enumerate(EXEC_LIST, start=1):
            print(f'{key}. {func["title"]}')
        id = int(input('Введите номер действия: ')) - 1
        if 0 <= id < len(EXEC_LIST):
            try:
                EXEC_LIST[id]['func_name']()
                if input('Для продолжения нажмите Enter: ') == '':
                    continue
                else:
                    break                           
            except Exception as e:
                print(e)
                continue_execution = False
        else:
            continue_execution = False
                                
        


if __name__ == '__main__':
    main()
