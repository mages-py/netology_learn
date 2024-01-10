import os

def get_sorted_file_list(dir_name):
    files = os.listdir(dir_name)
    sorted_files = {}
    for file in files:
        file_path = os.path.join(dir_name, file)
        if not os.path.isdir(file_path):
            sorted_files[file] = os.path.getsize(file_path)
    return dict(sorted(sorted_files.items(), key=lambda item: item[1]))

def create_sorted_file(dir_name, sorted_file_name, rewrite_sorted_file = True):
    if rewrite_sorted_file:
        open_mode = 'w'
    else: 
        open_mode = 'a'
    
    list_of_files = list(get_sorted_file_list(dir_name).keys())
    write_list = []
    for file in list_of_files:
        with open(os.path.join(dir_name, file), encoding='utf-8') as f:
            lines = f.readlines()
            write_list += [file + '\n', str(len(lines)) + '\n']
            write_list += lines
            write_list += ['\n']
    with open(sorted_file_name, encoding='utf-8', mode=open_mode) as wf:
        wf.writelines(write_list)
        


if __name__ == '__main__':
    dir_name = 'files/'
    sorted_file_name = 'new_file.txt'
    create_sorted_file(dir_name, sorted_file_name)
    with open(sorted_file_name, encoding='utf-8') as f:
        for line in f.readlines():
            print(line, end='')