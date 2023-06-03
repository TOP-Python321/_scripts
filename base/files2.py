from pathlib import Path
from re import sub

file_path = Path(r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\git.txt')


filein = open(file_path, encoding='utf-8')

print(filein, end='\n\n')

# работает по принципу генератора:
# читает очередную строку
# print(repr(filein.readline()))
# print(repr(filein.readline()))
# print(repr(filein.readline()))
# читает до конца
# print(repr(filein.read()))
# вернёт пустую строку — больше нечего читать
# print(repr(filein.readline()))

text = ''
for line in filein:
    text += line.strip() + '\n'

filein.close()

# text.replace('\n\n\n', '\n').replace('\n\n', '\n')
text_edit = sub(r'\n{2,}', '\n', text)

fileout = open(file_path.parent / 'git_new.txt', 'a', encoding='utf-8')
fileout.write(text_edit)
fileout.close()
