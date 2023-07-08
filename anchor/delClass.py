# -*- coding: utf-8 -*-
import os
import  tqdm

class delclass:
    def __init__(self, LaP):
        self.__LablePath = LaP
        pass

    def __GetFile(self, folder_path):
        file_names = []
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                file_names.append(file_name)
        return file_names
    
    def __delete_class(self,txt_name,class_name):
        # F5 0.24267582595348358 0.7631836533546448 0.03033468872308731 0.042038802057504654
        # 一个txt文件中有数行这样的数据，每行代表一个框，第一个数是类别，后面四个数是中心点坐标和宽高
        # 删除指定类别的框，比如删除类别为F5的框，即删除txt中每行第一个数为F5的行
        # 读取txt文件
        with open(txt_name, 'r') as f:
            lines = f.readlines()
        # 用于存储删除指定类别后的数据
        new_lines = []
        # 遍历每一行数据
        for line in lines:
            # 将每一行数据按空格分开
            parts = line.strip().split(' ')
            # 如果第一个数不是指定的类别，则将这一行数据添加到new_lines中
            if parts[0] != class_name:
                new_lines.append(line)
        # 将new_lines中的数据写入txt文件中
        with open(txt_name, 'w') as f:
            # 清空原txt文件中的数据
            f.truncate()
            # 将new_lines中的数据写入txt文件中
            f.writelines(new_lines)
    
    def __rem_class_dota(self,txt_name,class_name):
        # 827.5 625.1 912.4 537.8 928.0 553.0 843.1 640.3 W1 0
        # 前八个数是四个点的坐标，第九个数是类别，第十个数是难度
         # 删除指定类别的框，比如删除类别为F5的框，即删除txt中每行第一个数为F5的行
        # 读取txt文件
        with open(txt_name, 'r') as f:
            lines = f.readlines()
        # 用于存储删除指定类别后的数据
        new_lines = []
        # 遍历每一行数据
        for line in lines:
            # 将每一行数据按空格分开
            parts = line.strip().split(' ')
            # 如果第一个数不是指定的类别，则将这一行数据添加到new_lines中
            if parts[8] == class_name:
                new_lines.append(line)
        # 将new_lines中的数据写入txt文件中
        with open(txt_name, 'w') as f:
            # 清空原txt文件中的数据
            f.truncate()
            # 将new_lines中的数据写入txt文件中
            f.writelines(new_lines)

    def remain_class_dota(self,class_name):
        txt_file_names = self.__GetFile(self.__LablePath)
        for txt_file_name in tqdm.tqdm(txt_file_names):
            txt_file_path = os.path.join(self.__LablePath, txt_file_name)
            self.__rem_class_dota(txt_file_path,class_name)
    
    def del_class(self,class_name):
        txt_file_names = self.__GetFile(self.__LablePath)
        for txt_file_name in txt_file_names:
            txt_file_path = os.path.join(self.__LablePath, txt_file_name)
            self.__delete_class(txt_file_path,class_name)

    def __rem_class(self,txt_name,class_name):
        with open(txt_name, 'r') as f:
            lines = f.readlines()
        # 用于存储删除指定类别后的数据
        new_lines = []
        # 遍历每一行数据
        for line in lines:
            # 将每一行数据按空格分开
            parts = line.strip().split(' ')
            # 如果第一个数不是指定的类别，则将这一行数据添加到new_lines中
            if parts[0] == class_name:
                new_lines.append(line)
        # 将new_lines中的数据写入txt文件中
        with open(txt_name, 'w') as f:
            # 清空原txt文件中的数据
            f.truncate()
            # 将new_lines中的数据写入txt文件中
            f.writelines(new_lines)

    def remain_class(self,class_name):
        txt_file_names = self.__GetFile(self.__LablePath)
        for txt_file_name in tqdm.tqdm(txt_file_names):
            txt_file_path = os.path.join(self.__LablePath, txt_file_name)
            self.__rem_class(txt_file_path,class_name)

    


