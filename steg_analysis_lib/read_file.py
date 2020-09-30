
import cv2
import os

def read_file_name(path, name_or_namedir):
    
    file_list = os.listdir(path)
    file_list.sort()
    
    if(name_or_namedir == 'namedir'):
        for i in range(len(file_list)):
            file_list[i] = os.path.join(path, file_list[i])
    
    return file_list


def read_img(path):
    
    image = cv2.imread(path)
    
    cv2.imshow("original", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
	
    return image
    
    