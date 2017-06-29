from random import shuffle

import cv2
import keras
import numpy as np
import scipy.io as sio
import tensorflow as tf
import utility
from keras import backend as K
from keras import metrics
import model_ini

trainn = 102899
val = 5287
train_path = '/media/mjia/Data/SUN3D/train/'
val_path = '/media/mjia/Data/SUN3D/val/'

# input image dimensions
img_rows, img_cols = 448, 640
input_shape = (img_rows, img_cols, 6)
depth_shape = (img_rows, img_cols, 1)

# initialize the models
model_judge = model_ini.model_judgement(input_shape)

# compile the models
model_judge.compile(loss=utility.my_loss,
                  metrics=[utility.metric_L1_real],
                  optimizer=keras.optimizers.Adadelta())


# load weight

########################################### main ##################################################################
########################################### main ##################################################################
########################################### main ##################################################################
########################################### main ##################################################################
########################################### main ##################################################################
########################################### main ##################################################################
########################################### main ##################################################################