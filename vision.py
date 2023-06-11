import cv2 
import os
import numpy as np
 
thr=0.95
def custombasename(fullname):  
    return os.path.basename(os.path.splitext(fullname)[0])  
  
def GetFileFromThisRootDir(dir,ext = None):  
  allfiles = []  
  needExtFilter = (ext != None)  
  for root,dirs,files in os.walk(dir):  
    for filespath in files:  
      filepath = os.path.join(root, filespath)  
      extension = os.path.splitext(filepath)[1][1:]  
      if needExtFilter and extension in ext:  
        allfiles.append(filepath)  
      elif not needExtFilter:  
        allfiles.append(filepath)  
  return allfiles  
 
def visualise_gt(label_path, pic_path, newpic_path):
    results =  GetFileFromThisRootDir(label_path)
    for result in results:
        f = open(result,'r')
        lines = f.readlines()
        if len(lines)==0:  #如果为空
            print('文件为空',result)
            continue
        boxes = []
        for i,line in enumerate(lines):
            #score = float(line.strip().split(' ')[8])
            #if i in [0,1]:   #如果可视化DOTA-v1.5,前两行不需要，跳过，取消注释；如果可视化DOTA-v1.0,前两行需要，注释掉这两行代码
            #    continue
            name = result.split('/')[-1]
            box=line.strip().split(' ')[0:8]
            box = np.array(box,dtype = np.float64)
            #if float(score)>thr:
            boxes.append(box)
        boxes = np.array(boxes,np.float64)
        f.close()   
        filepath=os.path.join(pic_path, name.split('.')[0]+'.tif')
        im=cv2.imread(filepath)
        #print line3
        for i in range(boxes.shape[0]):
            box =np.array( [[boxes[i][0],boxes[i][1]],[boxes[i][2],boxes[i][3]], \
                            [boxes[i][4],boxes[i][5]],[boxes[i][6],boxes[i][7]]],np.int32)
            box = box.reshape((-1,1,2))
            cv2.polylines(im,[box],True,(0,0,255),2)
        cv2.imwrite(os.path.join(newpic_path,result.split('/')[-1].split('.')[0]+'.png'),im)
        #下面是有score的        
        #        x,y,w,h,score=box.split('_')#
        #        score=float(score)
        #        cv2.rectangle(im,(int(x),int(y)),(int(x)+int(w),int(y)+int(h)),(0,0,255),1)
        #        cv2.putText(im,'%3f'%score, (int(x)+int(w),int(y)+int(h)+5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
        #        cv2.imwrite(newpic_path+filename,im)
 
if __name__ == '__main__':
    pic_path = 'aug-images/' #样本图片路径
    label_path = 'aug-lables/'#DOTA标签的所在路径 
    # pic_path = 'images/' #样本图片路径
    # label_path = 'lables/'#DOTA标签的所在路径     
    newpic_path= 'vision/'  #可视化保存路径
    if not os.path.isdir(newpic_path):
        os.makedirs(newpic_path)
    visualise_gt(label_path, pic_path, newpic_path)
