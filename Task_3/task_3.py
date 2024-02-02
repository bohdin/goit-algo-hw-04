import colorama
import sys
import pathlib
def get_path():
    current_directory = sys.argv[1]
    
    # Створення об'єкта Path
    path = pathlib.Path(current_directory)
    
    path_visualization(path, 1)





def path_visualization(path, count):

    # Перевірка, чи директорія існує
    if not path.exists() or not path.is_dir():
        print(f"{path} не є дійсною директорією.")
        return

    # Виведення імен файлів та піддиректорій
    print(path.name)
    for item in path.iterdir():
        if item.is_dir():
            path_visualization(item, count+2)
        else:
            print(" "*count + item.name)

get_path()