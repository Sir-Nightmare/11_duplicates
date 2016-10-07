import os

import sys
import pytz


def are_files_duplicates(folder_path):
    set_of_files = set()
    list_of_dublicated_files = []
    for root_folder, sub_folders, file_names in os.walk(folder_path):
        for file_name in file_names:
            file_full_path = os.path.join(root_folder, file_name)
            file_size = os.path.getsize(file_full_path)
            name_size_of_the_file = file_name + str(file_size)
            if name_size_of_the_file not in set_of_files:
                set_of_files.add(name_size_of_the_file)
            else:
                list_of_dublicated_files.append([file_name, file_size, file_full_path])
    return list_of_dublicated_files


if __name__ == '__main__':
    # folder_path=sys.argv[1]
    folder_path = 'D:\groot_folder'
    are_files_duplicates(folder_path)
