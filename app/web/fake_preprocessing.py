from sklearn.neighbors import KNeighborsClassifier as KN
import csv
import matplotlib.pyplot as plt
import random
import numpy as np
from sklearn.model_selection import train_test_split


#임의 데이터 생성
Cdgree = []
amp = []
curr=[]
gas=[]
ffa_target = []
ffa_targetnp = []
for i in range(0,1000,1):
    for j in range(0,3,1):
        Cdgree.append(random.uniform(20.0,50.9))#온도
        amp.append(random.uniform(19.0,20.9))#습도
        curr.append(random.uniform(3,20.0))#전류값
        gas.append(random.uniform(0.0,200.0))#가스
        ffa_targetnp.append([0])
    
    
    Cdgree.append(random.uniform(48.0,120.9))#온도
    amp.append(random.uniform(0.0,20.9))#습도
    curr.append(random.uniform(15,30.0))#전류값
    gas.append(random.uniform(100.0,1000.0))#가스
    ffa_targetnp.append([1])

a = [random.uniform(20.0,120.9),random.uniform(0.1,20.9),random.uniform(3.0,30.0),random.uniform(10.0,1000.0)]
#2개의 클래스가 있고, 분류하는 이진분류이다.

ffa = np.column_stack((Cdgree,amp,curr,gas))
#데이터 전처리과정
#데이터 나누기

# total데이터중, test_size = 20%
train_input, test_input, train_target, test_target = train_test_split(
    ffa, ffa_targetnp, stratify=ffa_targetnp, random_state=42)

print(a)
kn = KN(n_neighbors=30)# n_neighbors는 근접이웃 개수
kn.fit(train_input, train_target)#모델
new = [40.2,10.1,20,2000]
print(kn.score(test_input,test_target))#정확도 
print(kn.predict([a]))#실데이터 in #정답 0 or 1
