import cv2 as cv
import numpy as np
from matplotlib  import pyplot as  plt

img1=cv.imread("st_logo.jpeg")
img1=cv.rotate(img1,cv.ROTATE_90_CLOCKWISE)

img1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)


img2=cv.imread("photo1.png")

img2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
sift=cv.xfeatures2d.SIFT_create()

kp1,ds1=sift.detectAndCompute(img1,None)
img1n=cv.drawKeypoints(img1,kp1,(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("sdf",img1n)


kp2,ds2=sift.detectAndCompute(img2,None)
FLANN_INDEX_KDTREE=1
counter=0
index_params=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_params=dict(checks=50)
flann=cv.FlannBasedMatcher(index_params,search_params)

matches=flann.knnMatch(ds1,ds2,k=2)
match_mask=[[0,0] for i in range(len(matches))]

for i,(m,n) in enumerate(matches):
 if m.distance<0.5*n.distance:
  match_mask[i]=[1,0]
  counter=counter+1

if(counter>10):
 print("got him   ",len(matches)," : ",counter)
new_img=cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,(0,0,255),(0,255,0),match_mask,flags=0)
cv.imwrite("matching.jpeg",new_img)
plt.imshow(new_img)
plt.show()


"""
obj=cv.ORB_create()
kp1,ds1=obj.detectAndCompute(img1,None)

kp2,ds2=obj.detectAndCompute(img2,None)

#performing brute force matching

bf=cv.BFMatcher(cv.NORM_HAMMING,crossCheck=False)
#matches=bf.match(ds2,ds1)
#matches = sorted(matches, key=lambda x:x.distance)
pairs_of_matches=bf.knnMatch(ds2,ds1,k=2)
pairs_of_matches = sorted(pairs_of_matches, key=lambda x:x[0].distance)
print(pairs_of_matches[0][0].distance)

matches = [x[0] for x in pairs_of_matches
 if len(x) > 1 and x[0].distance < 0.89 * x[1].distance]

New_img=cv.drawMatches(img1,kp1,img2,kp2,matches[:6],None,flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

plt.imshow(New_img)
plt.show()

"""











