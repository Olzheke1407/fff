import os

def split_file_path(file_path):
    
    directory, filename = os.path.split(file_path)

    
    name, extension = os.path.splitext(filename)

    return directory, name, extension


file_path = r"\Users\Public\BlueStacks.txt"
path, name, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)


