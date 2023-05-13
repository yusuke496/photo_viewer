from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import sys
import random

#get photo list
path=os.path.dirname(os.path.abspath(__file__))
#print(path)
path = path + "/photo_test/"
#print(path)
dir0 = os.listdir(path)
len0=len(dir0)
#print(dir0, dir0[0], len0)
dir1=[]
for i in range(0, len0):
    name = dir0[i]
    if name.count(".jpg") + name.count(".png") != 0:
        dir1.append(name)ss
    else:
        pass
#print(dir1)
len1=len(dir1)
n0 = random.randrange(0, len1)
photo=dir1[n0]
#print(photo)

#sys.exit()

#path=input("Input file name: ")
path=os.path.dirname(os.path.abspath(__file__))
#print(path)
path = path + "/photo_test/" + photo
#print(path)
a=os.path.exists(path)
if a==True :
        img = Image.open(path)
        #img.show()
        img_list = np.asarray(img)
        #img_list = np.array(img)
        #print(img_lis)
        plt.imshow(img_list)
        plt.show()
else :
    print("error")
