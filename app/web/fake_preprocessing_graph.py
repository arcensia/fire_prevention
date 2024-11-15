# import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier as KN
import csv
import matplotlib.pyplot as plt
import random
import numpy as np
from sklearn.model_selection import train_test_split



#임의 데이터 생성
Cdgree = []
amp = []
ffa_target = []
ffa_targetnp = []

for i in range(0,200,1):
# for j in range(0,3,1):
    Cdgree.append(random.uniform(20.0,50.9))#온도
    amp.append(random.uniform(19.0,20.9))#습도
    ffa_targetnp.append([1])
    
    
    Cdgree.append(random.uniform(48.0,120.9))#온도
    amp.append(random.uniform(0.0,20.9))#습도
    ffa_targetnp.append([0])


#2개의 클래스가 있고, 분류하는 이진분류이다.

ffa = np.column_stack((Cdgree,amp))
#데이터 전처리과정
#데이터 나누기

# total데이터중, test_size = 20%
train_input, test_input, train_target, test_target = train_test_split(
    ffa, ffa_targetnp, stratify=ffa_targetnp, random_state=42)

train_input = train_input


#스케일값 맞추기
mean = np.mean(train_input, axis = 0)#평균, axis축에서 0은 행(각 특성)두개의 값이 평균., 1은 각각 샘플마다 평균.열마다.
std = np.std(train_input, axis = 0)#표준편차
train_scaled = (train_input - mean)/std# == 표준점수
new =([120,10]-mean)/std# 수상한 데이터도 바꿔야지. 일반적으로 훈련세트와 똑같은 방식으로 한다.


kn = KN(n_neighbors=30)# n_neighbors는 근접이웃 개수
kn.fit(train_scaled, train_target)#모델
test_scaled = (test_input - mean)/std #항상 위와 맞춰주기.

print(kn.score(test_scaled,test_target))#정확도 
new = [0.5,0.2]
print(kn.predict([new]))#실데이터 in #정답 0 or 1

distances, indexes = kn.kneighbors([new])#근처 이웃 인덱스를 가져올 수 있다. #인덱스 번호가 있다.
plt.scatter(train_scaled[:,0],train_scaled[:,1])    
plt.scatter(test_scaled[:,0],test_scaled[:,1])
plt.scatter(new[0],new[1],marker='^')#세모로 표시
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1],marker='D')#첫번해 행 인덱스, 두번째 특성인 웨이트. 마름모로 표시.


# plt.ylim(100)#plt.xlim(100) #스케일 바꾸기.
plt.xlabel('Cdgree')
plt.ylabel('amp')
plt.show()