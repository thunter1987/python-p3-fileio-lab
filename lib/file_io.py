def write_file(file_name, file_content):
    open(file_name, 'w').write(file_content)
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as file_name:
        file_name.write(file_content)
        file_name.close()
        
def append_file(file_name, append_content):
    open(f'{file_name}.txt', 'a').write(append_content)
    with open('file_name.txt', mode='a', encoding='utf-8') as file_name:
        file_name.write(append_content)

def read_file(file_name):
    file = open(f'{file_name}.txt', encoding='utf-8')
    return file.read()
