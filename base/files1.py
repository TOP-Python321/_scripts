from pathlib import Path

file_path = Path(r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\git.txt')

git_description = file_path.read_text(encoding='utf-8')
# print(type(git_description), git_description, sep='\n')

new_file_path = file_path.parent / 'git_new.txt'

new_file_path.write_text(git_description[:267], encoding='utf-8')
