import pandas as pd
import numpy as np
import math
import sys
import os
fileName = sys.argv[1]
path = os.path.abspath('data')
df=pd.read_csv(path + '\\' + fileName)

total_rows=df['Views'].count()

view2=np.array([])
comments=np.array([])
likes=np.array([])

n = 152
if total_rows < n:
    n = total_rows

for i in range(1,n):
    view2=np.append(view2,df['Views'][i-1])
    comments=np.append(comments,df['Comments'][i])
    likes=np.append(likes,df['Likes'][i])

cmnt_square=comments*comments              #Storing square of comments in seperate column
cmnt_square_sum=np.sum(cmnt_square)        #storing sum of x1^2 where x1 is Comments
likes_square=likes*likes                   #Storing square of likes in seperate column
likes_square_sum=np.sum(likes_square)      #storing sum of x2^2 where x2 is Likes
view_cmnts=view2*comments                  #Storing the value of Views of next video * no of Comments as a seperate column
view_cmnts_sum=np.sum(view_cmnts)          #storing sum ofx1*y where x1 is no of Comments and y is no of Views for next video
view_like=view2*likes                      #Storing the value of Views of next video * no of Likes as a seperate column
view_like_sum=np.sum(view_like)            #storing sum ofx2*y where x2 is no of Likes and y is no of Views for next video
cmnts_likes=comments*likes                 #Storing the value of no of Comments * no of Likes as a seperate column
cmnts_likes_sum=np.sum(cmnts_likes)        #storing sum of x1*x2 where x1 is no of Comments and x2 is no of Likes

#The 6 lines are used as computation using these values would produce large values not able to evaluated by the computer.
#Even if we divide the final vaue remains the same as in the numerator and denominator 1000000 value gets cancelled

sx1s=float(cmnt_square_sum)#/1000000.0
sx2s=float(likes_square_sum)#/1000000.0
sx1y=float(view_cmnts_sum)#/1000000.0
sx2y=float(view_like_sum)
sx1x2=float(cmnts_likes_sum)


b1n=(sx2s*sx1y)-(sx1x2*sx2y)
b1d=(sx1s*sx2s)-(sx1x2*sx1x2)
#print(b1n,b1d)
b1=b1n/b1d                                  #computation for coefficient b1
b2n=(sx1s*sx2y)-(sx1x2*sx1y)
b2d=(sx1s*sx2s)-(sx1x2*sx1x2)

b2=b2n/b2d                                  #computation for coefficient b2

m1=np.average(comments)
m2=np.average(likes)
my=np.average(view2)

c=my-(b1*m1)-(b2*m2)                        #the required regression line passes through the means of both the independent variables .Using this we find c

#print('The regression equation used is y=b1x1+b2x2+c where...\n x1 is the present video comments...,\n x2 is present video likes and y is the next video views')
#print('The constant term c in the regression equation y=b1*x1+b2*x2+c is :',round(c,4))
#print('The coefficient b1 in the regression equation y=b1*x1+b2*x2+c is :',round(b1,4))
#print('The coefficient b2 in the regression equation y=b1*x1+b2*x2+c is :',round(b2,4))

np.append(comments,df['Comments'][0])
np.append(likes,df['Likes'][0])
np.append(view2,c+(b1*df['Comments'][0])+(b2*df['Likes'][0]))

print('The predicted number of views based on the previous videos comments and likes : ',math.floor(c+(b1*df['Comments'][0])+(b2*df['Likes'][0])))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cc,ll=np.meshgrid(comments,likes)
vv=c+b1*cc+b2*ll

plt3d=plt.figure().gca(projection='3d')
plt3d.scatter(comments,likes,view2,color='red')
plt3d.plot_surface(cc,ll,vv,color='black')
plt3d.set_xlabel('comments')
plt3d.set_ylabel('likes')
plt3d.set_zlabel('views')
plt.show()

sys.stdout.flush()