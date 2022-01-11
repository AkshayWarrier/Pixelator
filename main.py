import cv2
import numpy as np


img = cv2.imread("images\\flower.jpg")

 
pixelation = 12

l = []
for i in range(0,img.shape[0],pixelation):
    for j in range(0,img.shape[1],pixelation):
        s = img[i:i+pixelation,j:j+pixelation]
        sc = s.reshape((s.shape[0]*s.shape[1],3))
        r = [x[0] for x in sc]
        g = [x[1] for x in sc]
        b = [x[2] for x in sc]
        rm = int(np.mean(r))
        gm = int(np.mean(g))
        bm = int(np.mean(b))
        img[i:i+pixelation,j:j+pixelation] = (rm,gm,bm)
cv2.imwrite("images\\p.jpg",img)
cv2.imshow('Pixelator',img)

cv2.waitKey(0)
