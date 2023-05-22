with open('1.txt', encoding='utf-8') as file1, \
        open('2.txt', encoding='utf-8') as file2, \
        open('3.txt', encoding='utf-8') as file3, \
        open('file.txt', 'w', encoding='utf-8') as file4:
    dict_file = {'file1': file1.readlines(), 'file2': file2.readlines(), 'file3': file3.readlines()}
    file1.seek(0)
    file2.seek(0)
    file3.seek(0)
    dict_file1 = {'1.txt': len(file1.readlines()), '2.txt': len(file2.readlines()), '3.txt': len(file3.readlines())}
    sorted_tuple = sorted(dict_file1.items(), key=lambda x: x[1])
    for dict_file, sorted_tuple, dict_file1 in zip(sorted(dict_file.values(), reverse=True), sorted_tuple,
                                                   sorted(dict_file1.values())):
        file4.write(str(sorted_tuple[0]) + '\n')
        file4.write(str(dict_file1) + '\n')
        file4.write(''.join(dict_file) + '\n')
with open('file.txt', encoding='utf=8') as file4:
    print(file4.read())
