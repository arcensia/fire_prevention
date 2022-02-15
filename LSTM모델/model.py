from numpy.core.numerictypes import ScalarType
import tensorflow.keras.layers as layers
import tensorflow as tf
from tensorflow.python import keras
import numpy as np
# import matplotlib.pyplot as plt
from makedata import dummydata
import numpy as np
from sklearn.model_selection import train_test_split


time,raw_normal_data, raw_abnolmal_data = dummydata()
#shape : 20000, [2,20000]
#array[0, :] = sin
#array[1, :] = cos


#전처리
normal_data = np.array(raw_normal_data).reshape(20000,2)

normal_data_train = normal_data[:16000]
normal_data_test = normal_data[16000:]

abnormal_data = np.array(raw_abnolmal_data).reshape(20000,2)
abnormal_data_test = abnormal_data[:4000]


#테스트, 검증 데이터 만들기
normal_test_tot = np.hstack((normal_data_test, np.zeros(normal_data_test.shape[0]).reshape(-1,1)))
abnormal_test_tot = np.hstack((abnormal_data_test, np.ones(abnormal_data_test.shape[0]).reshape(-1,1)))
test_tot = np.vstack((normal_test_tot, abnormal_test_tot))
#데이터 분리
x_test, x_valid, y_test, y_valid = train_test_split(test_tot[:,:-1], test_tot[:,-1], test_size=0.3)

# print(x_test.shape)
# print(y_test.shape)
# print(x_valid.shape)
# print(y_valid.shape)

# (20000, 2)
# (5600, 2)
# (5600,)
# (2400, 2)
# (2400,)

#데이터 정규화
import sklearn.preprocessing as scaler
stder = scaler.StandardScaler()
stder.fit(normal_data_train)
x_normal_train_scaled = stder.transform(normal_data_train)
x_test_scaled = stder.transform(x_test)
x_valid_scaled = stder.transform(x_valid)


#데이터 차원 변경
x_normal_train_scaled = normal_data_train.reshape(x_normal_train_scaled.shape[0], 1 , x_normal_train_scaled.shape[1])
x_test_scaled = x_test.reshape(x_test_scaled.shape[0],1,x_test_scaled.shape[1])
x_valid_scaled = x_valid.reshape(x_valid_scaled.shape[0],1,x_valid_scaled.shape[1])
# print(x_nomal_train_scaled.shape)
# print(x_test_scaled.shape)
# print(x_valid_scaled.shape)
# (16000, 1, 2)
# (5600, 1, 2)
# (2400, 1, 2)

model = tf.keras.Sequential()

# model.add(layers.Embedding(2000,2,input_length = 100))
# model.add(layers.LSTM(8))
model.add(layers.LSTM(units = 10, activation='relu', input_shape=(x_normal_train_scaled.shape[1], x_normal_train_scaled.shape[2])))
model.add(layers.Dropout(rate = 0.2))
model.add(layers.Dense(units = 1))
model.compile(loss='mse', optimizer='adam', metrics=['mae'])
model.summary()
    
history = model.fit(x_normal_train_scaled, x_normal_train_scaled, epochs=3,batch_size=2)

# # def LSTM_MODEL(split_per_training):
# #     model = keras.Sequential()
# #     model.add(layers.LSTM(units=100,activation='relu',input_shape=[split_per_training,3]))
# #     model.add(layers.Dense(units=512))
# #     model.add(layers.Dense(units=1))
# #     model.compile(loss='mse', optimizer='adam', metrics=['mae'])
# #     model.summary()
# #     return model

# # history = model.fit(train_x,train_y,epochs=25,validation_split=0.25)
# # history = model.fit(train_x,train_y,validation_split=0.2,epochs=25) 


# model = layers.Sequential()
# #Adding the first LSTM layer and some Dropout regularisation
# model.add(layers.LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
# model.add(layers.Dropout(0.2))
# # Adding a second LSTM layer and some Dropout regularisation
# model.add(layers.LSTM(units = 50, return_sequences = True))
# model.add(layers.Dropout(0.2))
# # Adding a third LSTM layer and some Dropout regularisation
# model.add(layers.LSTM(units = 50, return_sequences = True))
# model.add(layers.Dropout(0.2))
# # Adding a fourth LSTM layer and some Dropout regularisation
# model.add(layers.LSTM(units = 50))
# model.add(layers.Dropout(0.2))
# # Adding the output layer
# model.add(layers.Dense(units = 1))
# # Compiling the RNN
# model.compile(optimizer = 'adam', loss = 'mean_squared_error')
# # Fitting the RNN to the Training set
# model.fit(X_train, y_train, epochs = 100, batch_size = 32)