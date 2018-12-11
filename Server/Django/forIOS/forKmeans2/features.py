import os
import tensorflow as tf
from tensorflow.python.platform import gfile

import numpy as np
import sklearn
import pickle

def get_feature(image):
    print(image)
    phone_features, phone_labels = extract_features(image)
    print("******extract features succeed******")
    print(phone_labels)
    print("******extract phone_labels succeed******")
    return phone_features


model_dir = '/home/deep/model/'
    
def create_graph():
    with gfile.FastGFile(os.path.join( model_dir, 'classify_image_graph_def.pb'), 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    
def extract_features(list_images):
    nb_features = 2048
    features = np.empty((len(list_images),nb_features))
    labels = []
    #print(root.encode("utf-8", "surrogateescape")) 
    create_graph()
    print("******graph loaded succeed*****")

    with tf.Session() as sess:

        next_to_last_tensor = sess.graph.get_tensor_by_name('pool_3:0')

        for ind, image in enumerate(list_images):
            #if (ind%1 == 0):
                #print('Processing %s...' % (image))
            if not gfile.Exists(image):
                tf.logging.fatal('File does not exist %s', image)

            #image_data = gfile.FastGFile(image, 'rb').read()
            image_data = list_images
            try:
                predictions = sess.run(next_to_last_tensor,{'DecodeJpeg/contents:0': image_data})
                features[ind,:] = np.squeeze(predictions)
                labels.append(re.split('_\d+',image.split('/')[0])[0])
            except:
                continue

    return features, labels
