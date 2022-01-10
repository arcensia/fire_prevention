from typing import Tuple
import numpy as np
import random
import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler

#정규화 #사실 필요없는데.
def minMaxScaler(data):
    Det = np.max(data,axis=0)-np.min(data,axis=0)
    num = data-np.min(data,axis=0)
    return num/Det

def dummydata():

    T = 100
    npx = np.array(np.linspace(0, T*np.pi*2, T*200, endpoint=True, retstep=False))
    npy = np.array([np.sin(2*npx), np.cos(2*npx)])

    train_sin = np.empty(len(npy[0]))
    train_con = np.empty(len(npy[1]))

    for x in range(0,len(npx),1):
        train_sin[x] = np.array([np.round_(random.uniform(npy[0,x]-0.1,npy[0,x]+0.1) ,5)])
        train_con[x] = np.array([np.round_(random.uniform(npy[1,x]-0.1,npy[1,x]+0.1) ,5)])

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

# # 1. 기본 스타일 설정
# plt.style.use('default')
# plt.rcParams['figure.figsize'] = (6, 3)
# plt.rcParams['font.size'] = 12
# plt.rcParams['lines.linewidth'] = 5

# x = np.linspace(-1, 1, 1000)
# y1 = np.sin(2 * x * np.pi)
# y2 = np.cos(2 * x * np.pi)
# y3 = np.ceil(3 * x)

# fig, ax = plt.subplots()

# # ax.spines['left'].set_position('center')        # 왼쪽 축을 가운데 위치로 이동
# # ax.spines['right'].set_visible(False)          # 오른쪽 축을 보이지 않도록
# # ax.spines['top'].set_visible(False)            # 위 축을 보이지 않도록
# # ax.spines['bottom'].set_position(('data', 0))   # 아래 축을 데이터 0의 위치로 이동
# # ax.tick_params('both', length=0)                # Tick의 눈금 길이 0

# ax.plot(x, y1, '--')
# ax.plot(x, y2, '-.')
# ax.plot(x, y3, alpha=0.7)

# # plt.show()
# plt.savefig('plotting2.png', dpi=200)
# plt.show()