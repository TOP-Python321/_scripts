# путь в *nix системах:
# '/home/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts/git.txt'

# путь в Windows
file_path1 = 'd:\\G-Doc\\YandexDisk\\Job\\TOP Academy\\Python web\\321\\scripts\\git.txt'
file_path2 = r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\git.txt'

print(file_path1)
print(file_path2)


from pathlib import Path


file_path3 = Path(r'd:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\git.txt')

# >>> file_path3
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts/git.txt')
# >>> 
# >>> file_path3.parent
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts')
# >>> 
# >>> file_path3.parents
# <WindowsPath.parents>
# >>> list(file_path3.parents)
# [WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts'), WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321'), WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web'), WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy'), WindowsPath('d:/G-Doc/YandexDisk/Job'), WindowsPath('d:/G-Doc/YandexDisk'), WindowsPath('d:/G-Doc'), WindowsPath('d:/')]
# >>>
# >>> 
# >>> file_path3.drive
# 'd:'
# >>>
# >>> file_path3.name
# 'git.txt'
# >>>
# >>> file_path3.parent.name
# 'scripts'
# >>>
# >>> file_path3.suffix
# '.txt'
# >>>
# >>> file_path3.parent.suffix
# ''
# >>>
# >>> file_path3.is_file()
# True
# >>> file_path3.is_dir()
# False
# >>>
# >>> file_path3.parent.is_dir()
# True
# >>> file_path3.parent.is_file()
# False
# >>>
# >>>
# >>> dir_path = file_path3.parent
# >>> dir_path
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts')
# >>>
# >>> file_path4 = dir_path / '.gitignore'
# >>> file_path4
# WindowsPath('d:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts/.gitignore')
# >>>
# >>> print(file_path4)
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\.gitignore
# >>>
# >>> file_path4.is_file()
# True
# >>> 
# >>>
# >>> dir_path.iterdir()
# <generator object Path.iterdir at 0x000001FE6F5997E0>
# >>> 
# >>> for p in dir_path.iterdir():
# ...     print(p)
# ...
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\.git
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\.gitignore
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\.idea
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\base
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\git.txt
# d:\G-Doc\YandexDisk\Job\TOP Academy\Python web\321\scripts\venv
# >>>
# >>>
# >>> from sys import path
# >>>
# >>> path[0]
# 'D:\\G-Doc\\YandexDisk\\Job\\TOP Academy\\Python web\\321\\scripts\\base'
# >>>
# >>> Path(path[0])
# WindowsPath('D:/G-Doc/YandexDisk/Job/TOP Academy/Python web/321/scripts/base')
# >>>
# >>> for file in Path(path[0]).iterdir():
# ...     if file.is_file():
# ...             print(file.name)
# ...
# 1.py
# cycle_nested1.py
# decorator1.py
# decorator2.py
# dict1.py
# dict2.py
# dict3.py
# dict4.py
# for1.py
# for2.py
# function1.py
# function2.py
# function3.py
# function4.py
# func_args1.py
# func_args2.py
# func_args3.py
# func_args4.py
# func_args5.py
# generator1.py
# generator2.py
# generator3.py
# generator_expr1.py
# generator_expr2.py
# generator_expr3.py
# hl_func1.py
# hl_func2.py
# hl_func3.py
# if1.py
# if2.py
# if3.py
# input1.py
# lambda1.py
# lambda2.py
# lambda3.py
# lambda4.py
# lists1.py
# module1.py
# module2.py
# module3.py
# module4.py
# mutable_objects.py
# namespace1.py
# namespace2.py
# namespace3.py
# operator_comp.py
# operator_is.py
# operator_logic1.py
# operator_logic2.py
# operator_math.py
# operator_walrus.py
# path1.py
# print1.py
# print2.py
# range1.py
# range2.py
# range3.py
# sequence1.py
# sequence2.py
# set1.py
# set2.py
# set3.py
# strings.py
# try1.py
# try2.py
# types1.py
# types2.py
# unpacking.py
# while1.py
# while2.py
# while3.py
# >>>