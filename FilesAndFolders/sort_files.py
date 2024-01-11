import os

def get_sorted_file_dict(dir_name):
    files = os.listdir(dir_name)
    sorted_files = {}
    for file in files:
        file_path = os.path.join(dir_name, file)
        if not os.path.isdir(file_path):
            with open(file_path, encoding='utf-8') as f:
                sorted_files[file] = f.readlines()
    return dict(sorted(sorted_files.items(), key=lambda item: len(item[1])))

def create_sorted_file(dir_name, sorted_file_name, rewrite_sorted_file = True):
    list_of_files = get_sorted_file_dict(dir_name)
    write_list = []
    
    for file, lines in list_of_files.items():
        with open(os.path.join(dir_name, file), encoding='utf-8') as f:
            write_list += [file + '\n', str(len(lines)) + '\n'] + lines + ['\n']
            
    mode = 'w' if rewrite_sorted_file else 'a'
    with open(sorted_file_name, encoding='utf-8', mode=mode) as wf:
        wf.writelines(write_list)
        


if __name__ == '__main__':
    dir_name = 'files/'
    sorted_file_name = 'new_file.txt'
    create_sorted_file(dir_name, sorted_file_name)
    with open(sorted_file_name, encoding='utf-8') as f:
        for line in f.readlines():
            print(line, end='')