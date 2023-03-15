import cv2
import numpy as np
import os
import tensorflow as tf


def to_grayscale(directory, todirectory):
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            img = cv2.imread(f,cv2.IMREAD_GRAYSCALE)            
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(todirectory+"/"+ os.path.basename(f),resized_image)


def create_negative_bg():
    for file_type in ['negative_dilbert_grayscale']:
        for img in os.listdir(file_type):           
            line = file_type+'/'+img+'\n'
            with open('negative.txt','a') as f:
                f.write(line)


"""
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0],[tf.config.experimental.VirtualDeviceConfiguration(memory_limit=300)])
  except RuntimeError as e:
    print(e)
"""

# disable usage of GPU

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#configuration = tf.compat.v1.ConfigProto()
#configuration.gpu_options.allow_growth = True
#session = tf.compat.v1.Session(config=configuration)

#to_grayscale("positive_dilbert/", "positive_dilbert_grayscale/")

#to_grayscale("negative_dilbert/", "negative_dilbert_grayscale/")
create_negative_bg()