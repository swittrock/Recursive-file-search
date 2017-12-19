from pathlib import Path
import shutil
import os

def file_search():
    while True:
        try:
            file = input('what is the path name?')
            file_path = Path(file)
            if file == '':
                break
            if file_path.exists():
                stage_two(file_path)
                break
            else:
                print('ERROR')
        except:
            print('ERROR')



def stage_two(file_path:Path):
        try:
            while True:
                try:
                    second = input('what command next?').strip().split()
                    if second[0] == 'N':
                        for x in (search_directory_by_name(file_path, second[1])):
                            print(x)
                        third_command(search_directory_by_name(file_path, second[1]))
                        break
                    elif second[0] == 'E':
                        for x in (search_extension(file_path, second[1])):
                            print (x)
                        third_command(search_extension(file_path, second[1]))
                        break
                    elif second[0] == 'S':
                        for x in (search_by_size(file_path, int(second[1]))):
                            print (x)
                        third_command(search_by_size(file_path,int(second[1])))
                        break
                    else:
                        print('ERROR')
                except:
                    print('ERROR')
        except:
            print('ERROR')


def third_command(file_path:list):
    while True:
        command = input('what action next?')
        if command == 'P': # working
            for x in file_path:
                print(x)
            break
        elif command =='F':
            for x in file_path:
                if x.suffix == '.txt':
                    file = open(str(x),'r')
                    print(file.readline())
                else:
                    print('that is not a text file')
            break
        elif command == 'D':
            for x in file_path:
                shutil.copyfile(str(x), str(x) + '.dup')
            break
        elif command == 'T':
            for x in file_path:
                os.utime(str(x), times=None)
            break
        else:
            print('ERROR')

## make it possible to search for names with spaces in them


def search_directory_by_name(pathname:Path, file_name:str):
    files_list = list(pathname.iterdir())
    results = []
    for element in files_list:
        if element.is_file() and (element.name == file_name):
            results.append(element)
        if element.is_dir():
            results.extend(search_directory_by_name(element, file_name))
    return results

def search_by_size(pathname:Path, size:int): #S
    files_list = list(pathname.iterdir())
    results = []
    for element in files_list:
        if element.is_file() and element.stat().st_size > int(size):
            results.append(element)
        elif element.is_dir():
            results.extend(search_by_size(element, int(size)))
    return results


def search_extension(pathname:Path, extension:str): #E
    files_list = list(pathname.iterdir())
    results = []

    for element in files_list:
        if element.is_file() and (element.suffix == extension or (element.suffix.split('.')[1])):
            results.append(element)
        if element.is_dir():
            results.extend(search_extension(element, extension))
    return results

#P is a simple function

def text_file_read_line(pathname:Path): #F
    if pathname.suffix == '.txt':
        x = open(str(pathname), 'r')
        return x.readline(0)
    else:
        print('that is not a valid file for this command')

def duplicate_file(filename:Path): #D
    shutil.copyfile(str(filename), str(filename)+'.dup')

file_search()


