import cv2
import numpy as np
 
from matplotlib import pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})



def divimg(im,factor):
    im2 = cv2.imread(im,cv2.COLOR_BGR2GRAY)
    plt.title(im)
    plt.imshow(im2)
    plt.show()
    
    a2 = np.true_divide(im2,factor)
    title=im+"factor"
    plt.title(title)
    plt.imshow(a2)
    plt.show()
    
    a=np.multiply(a2,factor)
    title="rec"+im
    dondesave="./issue5/imgfac/"+title
    plt.title(title)
    plt.imshow(a)
    plt.show()

def divimgw(im,factor):
    im2 = cv2.imread(im,cv2.COLOR_BGR2GRAY)
    #plt.title(im)
    #plt.imshow(im2)
    #plt.show()
    
    a2 = np.true_divide(im2,factor)
    #title=im+"factor"
    #plt.title(title)
    #plt.imshow(a2)
    #plt.show()
    
    a=np.multiply(a2,factor)
    title="rec"+im
    plt.title(title)
    plt.imshow(a)
    plt.show()
    
    title=im
    dondesave="../imgfac/"+title
    plt.imsave(dondesave, a)
    