import cv2
import numpy as np
 
from matplotlib import pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})



def divimg(im,factor):
    im2 = cv2.imread(im,-1)
    #im2 = cv2.imread(im)
    #im2== cv2.imread(im,-1)
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
    plt.title(title)
    plt.imshow(a)
    plt.show()

def divimgw(im,factor):
    im2 = cv2.imread(im,-1)
    im2 = im2.astype(np.float32)
    im2 -= 32768.0
    im2 = im2.astype(np.int16)
    im2 = im2//factor
    im2 = im2*factor
    im2 = im2.astype(np.float32)
    im2 += 32768.0
    im2 = im2.astype(np.uint16)
    dondesave="../imgfac/"+im
    cv2.imwrite(dondesave,im2)

    