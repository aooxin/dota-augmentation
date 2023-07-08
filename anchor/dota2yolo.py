# 将dota数据集转化为yolo数据集，忽略角度，只需要转化成yolo需要的格式即可


import os
import cv2
import numpy as np

class dota2yolo:
    def __init__(self, LaP, OutLaP):
        self.__LablePath = LaP
        self.__OutLaP = OutLaP
        pass

    def __GetFile(self, folder_path):
        file_names = []
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                file_names.append(file_name)
        return file_names
    
    def __GetBbox(self, txt_file_path):
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
        bbox = []
        for line in lines:
            parts = line.strip().split(',')
            category = parts[0].split()
            x1, y1, x2, y2, x3, y3, x4, y4, classes, diff = category[:]
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            x4 = float(x4)
            y1 = float(y1)
            y2 = float(y2)
            y3 = float(y3)
            y4 = float(y4)
            bbox.append([x1, y1, x2, y2, x3, y3, x4, y4, classes, diff])
        return bbox
    
    def d2y(self):
        txt_file_names = self.__GetFile(self.__LablePath)
        for txt_file_name in txt_file_names:
            txt_file_path = os.path.join(self.__LablePath, txt_file_name)
            bbox = self.__GetBbox(txt_file_path)
            txt_file_name = txt_file_name.split('.')[0]
            txt_file_name = txt_file_name + '.txt'
            txt_file_path = os.path.join(self.__OutLaP, txt_file_name)
            with open(txt_file_path, 'w') as f:
                for box in bbox:
                    x1, y1, x2, y2, x3, y3, x4, y4, classes, diff = box[:]
                    # 先转换成int
                    x1=int(x1)
                    x2=int(x2)
                    x3=int(x3)
                    x4=int(x4)
                    y1=int(y1)
                    y2=int(y2)
                    y3=int(y3)
                    y4=int(y4)
                    # 旋转框的四点坐标转换为中心点坐标和宽高，使用cv实现
                    rect=cv2.minAreaRect(np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]]))
                    x=rect[0][0]
                    y=rect[0][1]
                    w=rect[1][0]
                    h=rect[1][1]
                    f.write(str(classes) + ' ' + str(x/1024) + ' ' + str(y/1024) + ' ' + str(w/1024) + ' ' + str(h/1024) + '\n')
        pass
