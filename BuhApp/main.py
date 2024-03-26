import art
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def print_art_words(words: list):
    for word in words:
        print(art.text2art(word, space=2, font="rnd-small"))


print('Сегодня:', datetime.today().strftime("%d.%m.%Y"))


if __name__ == "__main__":
    calculate_salary()
    get_employees()
    
    
    print('===============================================Module ART===============================================>>')
    print_art_words(['netology', 'educational', 'platform', 'No. 1!'])
    print('===============================================Module ART===============================================<<')