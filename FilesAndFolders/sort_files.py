import os

def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def create_sorted_file(dir_name, new_file_name, reload_file = True):
    if reload_file:
        remove_file(new_file_name)
    
    list_of_files = os.listdir(dir_name)
    new_list = []
    
    for file in list_of_files:
        if not os.path.isdir(os.path.join(dir_name, file)):
            with open(os.path.join(dir_name, file), encoding='utf-8') as f:
                file_len = len(f.readlines())
                new_list.append({'file': file, 'len': file_len})
    files = sorted(new_list, key=lambda x: x['len'])
    with open(new_file_name, encoding='utf-8', mode='a') as wf:
        write_list = []
        for file in files:
            write_list += [file['file'] + '\n', str(file['len']) + '\n']
            with open(os.path.join(dir_name, file['file']), encoding='utf-8') as rf:
                write_list += rf.readlines()
                write_list += ['\n']
        wf.writelines(write_list)
        


if __name__ == '__main__':
    print(create_sorted_file('files/', 'new_file3.txt'))