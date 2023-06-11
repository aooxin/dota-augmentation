import random
import cv2
from matplotlib import pyplot as plt
from tqdm import tqdm
import albumentations as A
import shutil
import os
import time
import matplotlib.pyplot as plt
import numpy as np
import math

class aug:
    def __init__(self,ImP,LaP,OutImP,OutLaP):
        self.__ImagePath=ImP
        self.__LablePath=LaP
        self.__OutImP=OutImP
        self.__OutLaP=OutLaP
        pass

    def __GetFile(self,folder_path):
        file_names = []
        for file_name in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, file_name)):
                file_names.append(file_name)
        return file_names
    
    def __GetBbox(self,txt_file_path):
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
        bbox=[]
        for line in lines:
            parts = line.strip().split(',')
            category = parts[0].split()
            x1, y1, x2, y2, x3, y3, x4, y4,classes,diff = category[:]
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            x4 = float(x4)
            y1 = float(y1)
            y2 = float(y2)
            y3 = float(y3)
            y4 = float(y4)
            bbox.append([x1,y1,x2,y2,x3,y3,x4,y4,classes,diff])
        return bbox
    
    def __GetBbox2MirrorHorizon(self,txt_file_path,w):
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
        bbox=[]
        for line in lines:
            parts = line.strip().split(',')
            category = parts[0].split()
            x1, y1, x2, y2, x3, y3, x4, y4,classes,diff = category[:]
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            x4 = float(x4)
            y1 = float(y1)
            y2 = float(y2)
            y3 = float(y3)
            y4 = float(y4)
            space_separated_string = ' '.join(map(str, [w-x1,y1,w-x2,y2,w-x3,y3,w-x4,y4,classes,diff]))
            bbox.append(space_separated_string)
        return bbox
    
    def __GetBbox2Vertical(self,txt_file_path,h):
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
        bbox=[]
        for line in lines:
            parts = line.strip().split(',')
            category = parts[0].split()
            x1, y1, x2, y2, x3, y3, x4, y4,classes,diff = category[:]
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            x4 = float(x4)
            y1 = float(y1)
            y2 = float(y2)
            y3 = float(y3)
            y4 = float(y4)
            space_separated_string = ' '.join(map(str, [x1,h-y1,x2,h-y2,x3,h-y3,x4,h-y4,classes,diff]))
            bbox.append(space_separated_string)
        return bbox
    
    def __GetBbox2HV(self,txt_file_path,w,h):
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
        bbox=[]
        for line in lines:
            parts = line.strip().split(',')
            category = parts[0].split()
            x1, y1, x2, y2, x3, y3, x4, y4,classes,diff = category[:]
            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            x4 = float(x4)
            y1 = float(y1)
            y2 = float(y2)
            y3 = float(y3)
            y4 = float(y4)
            space_separated_string = ' '.join(map(str, [w-x1,h-y1,w-x2,h-y2,w-x3,h-y3,w-x4,h-y4,classes,diff]))
            bbox.append(space_separated_string)
        return bbox

    def __GetBboxRotate(self,txt_file_path,angle,w,h,d):
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()
        bbox=[]
        for line in lines:
            parts = line.strip().split(',')
            category = parts[0].split()
            x1, y1, x2, y2, x3, y3, x4, y4,classes,diff = category[:]
            # x1 = float(x1)
            # x2 = float(x2)
            # x3 = float(x3)
            # x4 = float(x4)
            # y1 = float(y1)
            # y2 = float(y2)
            # y3 = float(y3)
            # y4 = float(y4)
            # theta = math.radians(360-angle)
            cx=w/2
            cy=h/2
            cos = np.cos(np.deg2rad(360-angle))
            sin = np.sin(np.deg2rad(360-angle))
            x1 = float(x1)-cx
            x2 = float(x2)-cx
            x3 = float(x3)-cx
            x4 = float(x4)-cx
            y1 = float(y1)-cy
            y2 = float(y2)-cy
            y3 = float(y3)-cy
            y4 = float(y4)-cy
            new_x1 = round(x1 * cos - y1 * sin)
            new_y1 = round(x1 * sin + y1 * cos)
            new_x2 = round(x2 * cos - y2 * sin)
            new_y2 = round(x2 * sin + y2 * cos)
            new_x3 = round(x3 * cos - y3 * sin)
            new_y3 = round(x3 * sin + y3 * cos)
            new_x4 = round(x4 * cos - y4 * sin)
            new_y4 = round(x4 * sin + y4 * cos)
            new_x1 = new_x1+cx*d
            new_y1 = new_y1+cy*d
            new_x2 = new_x2+cx*d
            new_y2 = new_y2+cy*d
            new_x3 = new_x3+cx*d
            new_y3 = new_y3+cy*d
            new_x4 = new_x4+cx*d
            new_y4 = new_y4+cy*d
            space_separated_string = ' '.join(map(str, [new_x1,new_y1,new_x2,new_y2,new_x3,new_y3,new_x4,new_y4,classes,diff]))
            bbox.append(space_separated_string)
        return bbox

    def __lable2txt(self,lableInfo,txtPath):
        with open(txtPath, 'w') as f:
            f.writelines([line + os.linesep for line in lableInfo])

    def AddWeather(self):
        '''
        AddWeather:对文件夹中的图片进行天气增强 1:1:1:1=雨天:雪天:日光:阴影
        '''
        flag='000'
        Filelist=self.__GetFile(self.__ImagePath)
        for filename in tqdm(Filelist):
            name_only = os.path.splitext(os.path.basename(filename))[0]
            image = cv2.imread(self.__ImagePath+'/'+filename)
            height, width, _ = image.shape
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            random_number = random.randint(0, 3)
            # random_number=3
            if random_number==0:
                transform = A.Compose(
                    [A.RandomRain(brightness_coefficient=0.9, drop_width=1, blur_value=5, p=1)],
                )
            elif random_number==1:
                transform = A.Compose(
                    [A.RandomSnow(brightness_coeff=1.2, snow_point_lower=0.3, snow_point_upper=0.5, p=1)],
                )
            elif random_number==2:
                transform = A.Compose(
                    [A.RandomSunFlare(flare_roi=(0, 0, 1, 1), angle_lower=0.2, p=1)],
                )
            else:
                transform = A.Compose(
                    [A.RandomShadow(num_shadows_lower=1, num_shadows_upper=3, shadow_dimension=5, shadow_roi=(0, 0.5, 1, 1), p=1)],
                )
            random.seed(time.time())
            transformed = transform(image=image)
            # visualize(transformed['image'])
            cv2.imwrite(self.__OutImP+'/'+name_only+flag+'.tif',transformed['image'])
            shutil.copy(self.__LablePath+'/'+name_only+'.txt', self.__OutLaP+'/'+name_only+flag+'.txt')

    def MirrorHorizon(self,ratio=1.0):
        '''
        MirrorHorizon: 水平镜像图像
        ratio: float < 1.0
        '''
        flag='001'
        Filelist=self.__GetFile(self.__ImagePath)
        # if random_float<ratio:
        for filename in tqdm(Filelist):
            random_float = random.uniform(0, 1)
            if ratio<random_float:
                continue
            name_only = os.path.splitext(os.path.basename(filename))[0]
            image = cv2.imread(self.__ImagePath+'/'+filename)
            height, width, _ = image.shape
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # 水平镜像
            flipped = cv2.flip(image, 1)
            # 保存镜像后的图像文件
            cv2.imwrite(self.__OutImP+'/'+name_only+flag+'.tif', flipped)
            lableInfo=self.__GetBbox2MirrorHorizon(self.__LablePath+'/'+name_only+'.txt',width)
            self.__lable2txt(lableInfo,self.__OutLaP+'/'+name_only+flag+'.txt')

    def MirrorVertical(self,ratio=1.0):
        '''
        MirrorVertical: 竖直镜像图像
        ratio: float < 1.0
        '''
        flag='010'
        Filelist=self.__GetFile(self.__ImagePath)
        # if random_float<ratio:
        for filename in tqdm(Filelist):
            random_float = random.uniform(0, 1)
            if ratio<random_float:
                continue
            name_only = os.path.splitext(os.path.basename(filename))[0]
            image = cv2.imread(self.__ImagePath+'/'+filename)
            height, width, _ = image.shape
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # 竖直镜像
            flipped = cv2.flip(image, 0)
            # 保存镜像后的图像文件
            cv2.imwrite(self.__OutImP+'/'+name_only+flag+'.tif', flipped)
            lableInfo=self.__GetBbox2Vertical(self.__LablePath+'/'+name_only+'.txt',height)
            self.__lable2txt(lableInfo,self.__OutLaP+'/'+name_only+flag+'.txt')
    
    def MirrorHorizonAndVertical(self,ratio=1.0):
        '''
        MirrorHorizonAndVertical: 水平竖直镜像图像
        ratio: float < 1.0
        '''
        flag='011'
        Filelist=self.__GetFile(self.__ImagePath)
        # if random_float<ratio:
        for filename in tqdm(Filelist):
            random_float = random.uniform(0, 1)
            if ratio<random_float:
                continue
            name_only = os.path.splitext(os.path.basename(filename))[0]
            image = cv2.imread(self.__ImagePath+'/'+filename)
            height, width, _ = image.shape
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # 竖直镜像
            flipped = cv2.flip(image, -1)
            # 保存镜像后的图像文件
            cv2.imwrite(self.__OutImP+'/'+name_only+flag+'.tif', flipped)
            lableInfo=self.__GetBbox2HV(self.__LablePath+'/'+name_only+'.txt',width,height)
            self.__lable2txt(lableInfo,self.__OutLaP+'/'+name_only+flag+'.txt')

    def Rotate(self,angle=45,ratio=1.0):
        flag='100'
        Filelist=self.__GetFile(self.__ImagePath)
        # if random_float<ratio:
        for filename in tqdm(Filelist):
            random_float = random.uniform(0, 1)
            if ratio<random_float:
                continue
            name_only = os.path.splitext(os.path.basename(filename))[0]
            image = cv2.imread(self.__ImagePath+'/'+filename)
            height, width, _ = image.shape
            center = (width / 2, height / 2)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # 计算旋转矩阵
            matrix = cv2.getRotationMatrix2D(center, angle, 1)
            # 计算旋转后的图像大小
            cos = np.abs(matrix[0, 0])
            sin = np.abs(matrix[0, 1])
            new_width = int(height * sin + width * cos)
            new_height = int(height * cos + width * sin)
            # 调整旋转矩阵以考虑新的大小
            matrix[0, 2] += (new_width - width) / 2
            matrix[1, 2] += (new_height - height) / 2
            # 旋转图像并填充黑色
            rotated = cv2.warpAffine(image, matrix, (new_width, new_height), borderValue=(0, 0, 0))
            # 保存旋转后的图像文件
            cv2.imwrite(self.__OutImP+'/'+name_only+flag+'.tif', rotated)
            lableInfo=self.__GetBboxRotate(self.__LablePath+'/'+name_only+'.txt',angle,width,height,new_height/height)
            self.__lable2txt(lableInfo,self.__OutLaP+'/'+name_only+flag+'.txt')

    
            

        





            
            

            

            



    
        