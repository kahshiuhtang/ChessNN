import tensorflow as tf
from tensorflow import keras
from keras.layers import Input, Dense, Activation, Flatten, Conv2D, LayerNormalization, MaxPooling2D
import chess
import stockfish
import numpy as np


class NN():

  def __init__(self, path):
    self.input_shape = (8,8,12) # 6 Unique pieces for both sides
    self.model = self._create_model(Input(shape=self.input_shape))

  def _create_model(self, position, activ_func="relu"):
    dense1_1 = Dense(3072, activation=activ_func)(position)
    dense1_2 = Dense(3072, activation=activ_func)(dense1_1)
    dense1_3 = Dense(3072, activation=activ_func)(dense1_2)
    norm1 = LayerNormalization(axis=1)(dense1_3)

    conv2_1 = Conv2D(8, kernel_size=(2, 2), activation=activ_func)(position)
    conv2_2 = Conv2D(16, kernel_size=(2, 2), activation=activ_func)(conv2_1)
    conv2_3 = Conv2D(32, kernel_size=(2, 2), activation=activ_func)(conv2_2)
    conv2_4 = Conv2D(64, kernel_size=(2, 2), activation=activ_func)(conv2_3) 
    norm2 =  LayerNormalization(axis=1)(conv2_4)
    pooling2 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm2)
    flat2 = Flatten()(conv2_4)

    conv3_1 = Conv2D(8, kernel_size=(3, 3), activation=activ_func)(position)
    conv3_2 = Conv2D(16, kernel_size=(3, 3), activation=activ_func)(conv3_1)
    conv3_3 = Conv2D(32, kernel_size=(3, 3), activation=activ_func)(conv3_2)
    conv3_4 = Conv2D(64, kernel_size=(3, 3), activation=activ_func)(conv3_3) 
    norm3 =  LayerNormalization(axis=1)(conv3_4) 
    pooling3 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm3)
    flat3 = Flatten()(conv3_4)

    conv4_1 = Conv2D(8, kernel_size=(4, 4), activation=activ_func)(position)
    conv4_2 = Conv2D(16, kernel_size=(4, 4), activation=activ_func)(conv3_1)
    conv4_3 = Conv2D(32, kernel_size=(4, 4), activation=activ_func)(conv3_2) 
    norm4 =  LayerNormalization(axis=1)(conv4_3)
    pooling4 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm4)
    flat4 = Flatten()(conv4_3)

    conv5_1 = Conv2D(8, kernel_size=(5, 5), activation=activ_func)(position)
    conv5_2 = Conv2D(16, kernel_size=(5, 5), activation=activ_func)(conv5_1)
    conv5_3 = Conv2D(32, kernel_size=(5, 5), activation=activ_func)(conv5_2)  
    norm5 =  LayerNormalization(axis=1)(conv5_3)
    pooling5 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm5)
    flat5 = Flatten()(conv5_3)

    conv6_1 = Conv2D(8, kernel_size=(6, 6), activation=activ_func)(position)
    conv6_2 = Conv2D(16, kernel_size=(6, 6), activation=activ_func)(conv6_1)
    norm6 =  LayerNormalization(axis=1)(conv6_2)
    pooling6 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm6)
    flat6 = Flatten()(conv6_2)

    conv7_1 = Conv2D(8, kernel_size=(7, 7), activation=activ_func)(position)
    conv7_2 = Conv2D(16, kernel_size=(7, 7), activation=activ_func)(conv7_1)
    norm7 =  LayerNormalization(axis=1)(conv7_2)
    pooling7 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm7)
    flat7 = Flatten()(conv7_2)

    conv8_1 = Conv2D(8, kernel_size=(8,8), activation=activ_func)(position)
    norm8 =  LayerNormalization(axis=1)(conv8_1)
    pooling8 = MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid", data_format=None)(norm8)
    flat8 = Flatten()(conv8_1)

    model = keras.layers.concatenate([])
    return model
