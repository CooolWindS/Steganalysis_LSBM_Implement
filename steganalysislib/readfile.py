
import cv2
import os

def read_file_name(path, name_or_namedir):
    
    fileList = os.listdir(path)
    fileList.sort()
    
    if(name_or_namedir == 'namedir'):
        for i in range(len(fileList)):
            fileList[i] = os.path.join(path, fileList[i])
    
    return fileList


def read_img(path):
    
    image = cv2.imread(path)
    
    cv2.imshow("original", image)
    cv2.waitKey(0)
    
    (B,G,R) = cv2.split(image)#提取R、G、B分量
    cv2.imshow("Red",R)
    cv2.imshow("Green",G)
    cv2.imshow("Blue",B)
    cv2.waitKey(0)
    