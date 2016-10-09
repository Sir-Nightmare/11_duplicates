import os
from tabulate import tabulate
import sys


def find_file_duplicates(folder_path):
    set_of_files = set()
    list_of_duplicated_files = []
    for root_folder, sub_folders, file_names in os.walk(folder_path):
        for file_name in file_names:
            file_full_path = os.path.join(root_folder, file_name)
            file_size = os.path.getsize(file_full_path)
            name_size_of_the_file = file_name + str(file_size)
            if name_size_of_the_file not in set_of_files:
                set_of_files.add(name_size_of_the_file)
            else:
                list_of_duplicated_files.append([file_name, file_size, file_full_path])
    return list_of_duplicated_files


def print_list_of_duplicates(list_of_duplicated_files):
    print('The list of duplicated files:')
    print(tabulate(list_of_duplicated_files,
                   headers=['File name', 'Size in bytes', 'Full path to the file'], tablefmt="orgtbl"))


def delete_files(list_to_delete):
    for file in list_to_delete:
        os.unlink(file[2])


if __name__ == '__main__':
    folder_path = sys.argv[1]
    list_of_duplicated_files = find_file_duplicates(folder_path)
    if len(list_of_duplicated_files) > 0:
        print_list_of_duplicates(list_of_duplicated_files)
        are_to_delete = input('\nDo you want do delete all duplicates permanently? (y/n)\n')
        if are_to_delete == 'y':
            delete_files(list_of_duplicated_files)
            print('All duplicated files were permanently deleted.')
    else:
        print('There is no duplicated files.')
