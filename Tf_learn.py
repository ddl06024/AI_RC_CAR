from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from keras.callbacks import EarlyStopping
from keras.utils import np_utils

import numpy as np
import tensorflow as tf
from get_image_data import *

from keras.callbacks import EarlyStopping

class DNN_Driver():
    def __init__(self):
        self.trX = None
        self.trY = None
        self.teX = None
        self.teY = None
        self.model = None
        ###
        self.model_2 = None

    def tf_learn(self):
        self.trX, self.trY = get_training_data()
        self.teX, self.teY = get_test_data()

        seed = 0
        np.random.seed(seed)
        tf.random.set_seed(seed)
        early_stopping = EarlyStopping(monitor = 'val_loss', min_delta = 0, patience = 0, verbose = 0, mode = 'auto')

        self.model=Sequential()
        self.model.add(Dense(300, input_dim=np.shape(self.trX)[1], activation='relu'))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dense(1))
        self.model.compile(loss='mean_squared_error', optimizer= 'adam' )
        self.model.fit(self.trX, self.trY, epochs=3, batch_size=1,validation_data = (self.teX,self.teY),callbacks = [early_stopping])
        return
def tf_learn_2(self):
        
        self.trX, self.trY = get_training_data_2()
        self.teX, self.teY = get_test_data_2()
        
        self.trY = np_utils.to_categorical(self.trY,7)
        
        self.teY = np_utils.to_categorical(self.teY,7 )

        seed = 0
        np.random.seed(seed)
        tf.random.set_seed(seed)

        ## cnn model

        self.model_2 = Sequential()

        self.model_2.add(Conv2D(16, kernel_size = (3,3), input_shape=(16,16,1), activation = 'relu'))
        self.model_2.add(Conv2D(8,(3,3), activation = 'relu'))
        #self.model_2.add(Conv2D(16,(3,3), activation = 'relu'))
        self.model_2.add(MaxPooling2D(pool_size = 1))
        self.model_2.add(Dropout(0.25))
        self.model_2.add(Flatten())
        self.model_2.add(Dense(128, activation = 'relu'))
        self.model_2.add(Dropout(0.5))
        self.model_2.add(Dense(7, activation = 'softmax'))
        self.model_2.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
        self.model_2.fit(self.trX, self.trY,validation_data = (self.teX,self.teY),epochs = 2, batch_size = 1 )
        
        return

def predict_direction(self, img):
        print(img.shape)
#        img = np.array([np.reshape(img,img.shape**2)])
        ret =  self.model.predict(np.array([img]))
        print("print ret{0}".format(ret))
        return ret
def predict_direction_2(self,img):
      
        self.categories = [-1.0, -0.8 , -0.3 , 0.0 , 0.3, 0.8, 1.0]
        
        print(img.shape)
        img = np.array([np.reshape(img,(16,16,1))]) # cnn model -> 16 x 16

        #ret = self.categories[self.model_2.predict_classes(img)]
        ret = self.model_2.predict(img).argmax()
        print( "ret : {0}".format(ret))
        
        ret = self.categories[ret]
        print( "ret : {0}".format(ret))
        
        return ret

def get_test_img(self):
    img = self.teX[10]
    return img
