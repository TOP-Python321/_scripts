from pathlib import Path
from re import findall

file_path = Path(r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\git.txt')

with open(file_path, encoding='utf-8') as filein:
    text = filein.read()
# файлопоток уже закрыт


substrings = findall(
    r'\n.*?(?P<step>шаг \d{1,2}: .*?)\n',
    text
)
text = '\n'.join(sorted(substrings))

new_file_path = file_path.parent / 'git_new.txt'
with open(new_file_path, 'w', encoding='utf-8') as fileout:
    fileout.write(text)
# файлопоток уже закрыт

