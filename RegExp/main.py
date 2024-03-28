from pprint import pprint
import csv
import re

def normalize_phone(phone):
    ...
    pattern = re.compile(r'(8|\+7)?\s((\d+))\s(\d+)[\s-](\d+)[\s-](\d+)')
    res = pattern.search(phone)
    if res:
        return '+7' + res.group(2) + res.group(3) + res.group(4) + res.group(5)
    
    

# читаем адресную книгу в формате CSV в список contacts_list
def normalize_phonebook():
    with open("assets/phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    dict_phonebook = {}
    for row in contacts_list[1:]:
        fio = ' '.join([x.strip() for x in row[0:3] if x]).split()
        key = '_'.join(fio[:2])
        if key not in dict_phonebook:
            dict_phonebook[key] = {
                'lastname': fio[0],  
                'firstname': fio[1],
                'surname': fio[2] if len(fio) > 2 else '',
                'organization': row[3],
                'position': row[4],
                'phone': row[5],
                'email': row[6],
            }
        else:
            if len(fio) > 2:
                dict_phonebook[key]['surname'] = fio[2]
            if not dict_phonebook[key]['organization']:
                dict_phonebook[key]['organization'] = row[3]
            if not dict_phonebook[key]['position']:
                dict_phonebook[key]['position'] = row[4]
            if not dict_phonebook[key]['phone']:
                dict_phonebook[key]['phone'] = row[5]
            if not dict_phonebook[key]['email']:
                dict_phonebook[key]['email'] = row[6]
        pprint(dict_phonebook)

if __name__ == "__main__":
    normalize_phone('+7 (495) 913-04-78')