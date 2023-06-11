import os.path

with open('1.txt', encoding='utf-8') as file1,open('2.txt', encoding='utf-8') as file2, open('3.txt', encoding='utf-8') as file3:
    text1 = file1.readlines()
    text1.insert(0, os.path.basename(r'C:\Users\User\Desktop\rw_files\1.txt'))
    text2 = file2.readlines()
    text2.insert(0, os.path.basename(r'C:\Users\User\Desktop\rw_files\2.txt'))
    text3 = file3.readlines()
    text3.insert(0, os.path.basename(r'C:\Users\User\Desktop\rw_files\3.txt'))

with open('4.txt', 'w', encoding='utf-8') as file4:
    text4 = [text1, text2, text3]
    text4.sort(key=len)
    for text in text4:
        file4.write('\n')
        file4.write(text[0])
        file4.write('\n')
        file4.write(str(len(text[1:])))
        file4.write('\n')
        file4.writelines(text[1:])