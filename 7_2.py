from pprint import pprint
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    start = 0
    start_ = file.seek(0)
    #print(string_positions)

    for string_ in strings:
        file.write(string_+'\n')
        start += 1
        key = (start, start_)
        #print(key)
        string_positions[key]= string_
        #print(string_)
        start_ = file.tell()
    file.close()

    return string_positions

if __name__ == "__main__":

    info = ['Text for tell.','Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
