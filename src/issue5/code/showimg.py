import cv2
import numpy as np
 
from matplotlib import pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})


def showimg(im):
    im2 = cv2.imread(im,cv2.COLOR_BGR2GRAY)
    plt.title(im)
    plt.imshow(im2)
    plt.show()
    im="../imgfac/"+im
    im2 = cv2.imread(im,cv2.COLOR_BGR2GRAY)
    plt.title(im)
    plt.imshow(im2)
    plt.show()