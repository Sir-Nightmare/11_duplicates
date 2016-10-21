import argparse
import os
from datetime import datetime


def find_all_files(folder_path):
    all_files = {}
    number_of_duplicate_groups = 0
    for root_folder, sub_folders, file_names in os.walk(folder_path):
        for file_name in file_names:
            full_path = os.path.join(root_folder, file_name)
            file_size = os.path.getsize(full_path)
            name_size_of_the_file = '{}, size: {} bytes'.format(file_name, str(file_size))
            date_of_creation = datetime.fromtimestamp(os.path.getctime(full_path)).isoformat(
                sep=' ')
            if name_size_of_the_file in all_files:
                all_files[name_size_of_the_file].append((date_of_creation, full_path))
                if len(all_files[name_size_of_the_file]) == 2:
                    number_of_duplicate_groups += 1
            else:
                all_files[name_size_of_the_file] = [(date_of_creation, full_path)]
    return all_files, number_of_duplicate_groups


def print_duplicates_group(file_name, list_of_files_info):
    print(file_name)
    num_of_piece = 1
    for piece_of_info in list_of_files_info:
        print('{0:60s}{1:^6d}{2:30s}{3:50s}'.format(' ', num_of_piece, piece_of_info[0],
                                                    piece_of_info[1]))
        num_of_piece += 1


def print_table_header():
    print('{0:60s}{1:^6s}{2:30s}{3:50s}'.format('File', '#', 'Date', 'Full path'))
    print('-' * 165)


def print_all_duplicated_files_info(all_files):
    print('\nList of duplicate files:\n')
    print_table_header()
    for file_name, list_of_files_info in all_files.items():
        if len(list_of_files_info) > 1:
            print_duplicates_group(file_name, list_of_files_info)


def delete_duplicate_files_from_group(list_to_delete):
    for file_info in list_to_delete[1:]:
        os.unlink(file_info[1])


def delete_all_duplicates(all_files, is_the_newest_left):
    for file_name, list_of_files_info in all_files.items():
        if len(list_of_files_info) > 1:
            list_of_files_info.sort(reverse=is_the_newest_left)
            delete_duplicate_files_from_group(list_of_files_info)


def delete_chosed_files(list_of_files_info, file_to_delete_numbers):
    for num in file_to_delete_numbers:
        os.unlink(list_of_files_info[num][1])


def delete_all_duplicates_except_the_oldest(all_files):
    is_the_newest_file_left = False
    delete_all_duplicates(all_files, is_the_newest_file_left)


def delete_all_duplicates_except_the_newest(all_files):
    is_the_newest_file_left = True
    delete_all_duplicates(all_files, is_the_newest_file_left)


def manual_delete_files(all_files):
    for file_name, list_of_files_info in all_files.items():
        if len(list_of_files_info) > 1:
            print_table_header()
            print_duplicates_group(file_name, list_of_files_info)
            file_to_delete_numbers = [int(i) - 1 for i in input('Input numbers of files which you '
                                                                'want do delete. Separate numbers '
                                                                'with a space\n').split()]
            file_to_delete_numbers.sort()
            delete_chosed_files(list_of_files_info, file_to_delete_numbers)


def parsing_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Input full path to folder')
    parser.add_argument('-d', '--delete', default='manual', choices=['new', 'old', 'manual'],
                        help='choose which duplicates will be deleted (old/new/manual)')
    args = parser.parse_args()
    return args.path, args.delete


def ask_for_decision():
    decision = input("How do you want to delete the files? Choose one option:\n"
                     "'m' - delete manually\n"
                     "'new' - delete automatically, LEAVE THE OLDEST file in group\n"
                     "'old' - delete automatically, LEAVE THE NEWEST file in group\n"
                     "'p' - print the list of duplicated files\n")
    return decision


if __name__ == '__main__':
    folder_path, del_type = parsing_args()
    all_files, number_of_duplicate_groups = find_all_files(folder_path)
    if not number_of_duplicate_groups:
        print('There is no duplicate files.')
    else:
        print('There are {0} groups of duplicates.\n'.format(number_of_duplicate_groups))
        if del_type == 'manual':
            del_type = ask_for_decision()
        choise = {'m': manual_delete_files,
                  'new': delete_all_duplicates_except_the_oldest,
                  'old': delete_all_duplicates_except_the_newest,
                  'p': print_all_duplicated_files_info}
        choise[del_type](all_files)
        print('\nAll groups of duplicated files were treated')
