import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer, tokenizer_from_json
from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import efficientnet.tfkeras as efn
import numpy as np
import json

model = efn.EfficientNetB3(weights='imagenet', include_top = False, input_shape = (300,300,3), pooling = max)

Model = tf.keras.Model(
inputs = model.input,
outputs = keras.layers.GlobalAveragePooling2D()(model.output))

caption_model = load_model('Models/model.h5')

with open('Models/tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)

def img_features(image_path):
    # Load the image
    image = load_img(image_path, target_size=(300, 300))
    # Convert the image to an array
    image = img_to_array(image)
    image = image/255.
    image = np.expand_dims(image,axis=0)
    feature = Model.predict(image, verbose=0)
    return feature

def idx_to_word(integer,tokenizer):
    
    for word, index in tokenizer.word_index.items():
        if index==integer:
            return word
    return None

def predict_caption(image):
    
    feature = img_features(image)
    print(feature)
    in_text = "startseq"
    for i in range(34):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], 34)

        y_pred = caption_model.predict([feature,sequence])
        y_pred = np.argmax(y_pred)
        
        word = idx_to_word(y_pred, tokenizer)
        
        if word is None:
            break
            
        in_text+= " " + word
        
        if word == 'endseq':
            break
            
    in_text = in_text.rstrip('endseq')
    in_text = in_text.lstrip('startseq')
    return in_text