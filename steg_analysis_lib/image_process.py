
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


def extract_img_rgb(image):
	
    (B,G,R) = cv2.split(image)#提取R、G、B分量
    #cv2.imshow("Red",R)
    #cv2.imshow("Green",G)
    #cv2.imshow("Blue",B)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
	
    return (R, G, B)

def caculate_img_hist(image):
    
    hist = cv2.calcHist([image], [0], None, [256], [0,256])
    hist = np.reshape(hist, (256))
    
    return hist