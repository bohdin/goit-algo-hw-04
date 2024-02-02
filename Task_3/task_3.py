import colorama
import sys
from pathlib import Path

def get_path():
    # Отримання шляху з аргументів командного рядка
    current_directory = sys.argv[1]
    
    # Створення об'єкта Path
    path = Path(current_directory)
    
    # Перевірка, чи директорія існує
    if not path.exists() or not path.is_dir():
        print(f"{colorama.Fore.RED}{path} не є дійсною директорією.{colorama.Style.RESET_ALL}")
        return
    
    # Виклик функції для візуалізації структури
    path_visualization(path)





def path_visualization(path, indent=''):
    # Виведення імен файлів та піддиректорій
    print(f'{indent}{colorama.Fore.BLUE}[]{path.name}{colorama.Style.RESET_ALL}')

    # Проходимо по елементам директорії
    for item in path.iterdir():
        if item.is_dir():
             # Рекурсивний виклик для піддиректорій
            path_visualization(item, indent + ' |')
        else:
            # Виведення файлів
            print(f'{indent} | - {colorama.Fore.YELLOW}{item.name}{colorama.Style.RESET_ALL}')

get_path()