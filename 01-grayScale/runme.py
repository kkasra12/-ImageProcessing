import cv2
import numpy as np

image = cv2.imread('./sample.jpeg')
w=500
image = cv2.resize(image,(w,image.shape[0]*w//image.shape[1]))
grayV1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h,w,channel=image.shape
grayV2=np.zeros((h,w,1))
difimg=np.zeros((h,w,1))
differences=[]
for i,line in enumerate(image):
    for j,pixel in enumerate(line):
        y=int(0.299*pixel[2]+0.587*pixel[1]+0.144*pixel[0])
        grayV2[i][j]=y
        differences.append(abs(grayV1[i][j]-y))
        difimg[i][j]=abs(grayV1[i][j]-y)*5
print(f"mean:{sum(differences)/len(differences):0.3f}\n"+
      f"max:{max(differences)}\n"+
      f"min:{min([i for i in differences if i])}\n"+
      f"numberOfSamePixels: {differences.count(0)}~{h*w/differences.count(0):3f}%")
cv2.imwrite('grayscaleWithoutOpencv.jpg',grayV2)
cv2.imwrite('grayscaleWithOpencv.jpg',grayV1)
cv2.imwrite('difimg.jpg',difimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
