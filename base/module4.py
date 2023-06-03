from pathlib import Path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec

# путь к импортируемому файлу
importing_file_path = Path(path[0]) / '1.py'
# название модуля — будет использоваться в качестве атрибута модуля и ключа в системном словаре
module_name = 'тестовый модуль'
# создание объекта спецификации
spec = spec_from_file_location(module_name, importing_file_path)
# создание объекта модуля
test_module = module_from_spec(spec)
# добавление модуля в системный словарь
modules[module_name] = test_module
# выполнение модуля
spec.loader.exec_module(test_module)

