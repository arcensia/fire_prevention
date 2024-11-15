from typing import Tuple
import numpy as np
import random
import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler

#정규화
def minMaxScaler(data):
    Det = np.max(data,axis=0)-np.min(data,axis=0)
    num = data-np.min(data,axis=0)
    return num/Det

def dummydata():

    T = 10
    npx = np.array(np.linspace(0, T*np.pi*2, T*2000, endpoint=True, retstep=False))
    npy = np.array([np.sin(2*npx), np.cos(2*npx)])

    train_sin = np.empty(len(npy[0]))
    train_con = np.empty(len(npy[1]))

    for x in range(0,len(npx),1):
        train_sin[x] = np.array([np.round_(random.uniform(npy[0,x]-0.1,npy[0,x]+0.1) ,5)])
        train_con[x] = np.array([np.round_(random.uniform(npy[1,x]-0.2,npy[1,x]+0.2) ,5)])

    time = np.arange(len(npx))
    # train_y = minMaxScaler(train_y)
    adnomal = np.array([train_sin,train_con])
    
    return time, npy, adnomal

if __name__ == "__main__":
    xx, yy, zz= dummydata()

    print(xx.shape)
    print(yy.shape)
    print(zz.shape)
    # plt.scatter(x, y)
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.show()
