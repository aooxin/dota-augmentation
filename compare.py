# -*- coding: utf-8 -*-
import os

def get_filenames_without_extension(folder_path):
    filenames = os.listdir(folder_path)
    filenames_without_extension = set(os.path.splitext(file)[0] for file in filenames)
    return filenames_without_extension

def compare_folders(folder_path_1, folder_path_2):
    folder_1_files = get_filenames_without_extension(folder_path_1)
    folder_2_files = get_filenames_without_extension(folder_path_2)

    missing_in_folder_1 = folder_2_files - folder_1_files
    missing_in_folder_2 = folder_1_files - folder_2_files

    return missing_in_folder_1, missing_in_folder_2

def main():
    folder_path_1 = '/home/user/Dataset/aug-98-0627/images'  # ���滻Ϊ���ĵ�һ���ļ���·��
    folder_path_2 = '/home/user/Dataset/aug-98-0627/labelTxt'  # ���滻Ϊ���ĵڶ����ļ���·��

    missing_in_folder_1, missing_in_folder_2 = compare_folders(folder_path_1, folder_path_2)

    print(f'Missing in folder 1: {missing_in_folder_1}')
    print(f'Missing in folder 2: {missing_in_folder_2}')

if __name__ == '__main__':
    main()