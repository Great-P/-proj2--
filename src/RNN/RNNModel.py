""" Construct the RNN model for deep learning
"""

import keras
from keras import regularizers
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM, Masking, Embedding
from keras.optimizers import Adam


def RNN_model():
    SEG_LENTH = 180
    model = Sequential()
    model.add(Masking(mask_value=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
                      input_shape=(SEG_LENTH, 12)))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2, \
                   # kernel_regularizer = regularizers.l2(0.1),\
                   input_shape=(SEG_LENTH, 12), return_sequences=True))
    model.add(LSTM(64, dropout=0.2, recurrent_dropout=0.2, \
                   # kernel_regularizer = regularizers.l2(0.1),
                   return_sequences=True))
    model.add(LSTM(2))
    model.add(Activation('softmax'))
    adam = Adam()
    model.compile(loss='categorical_crossentropy', optimizer=adam, \
                  metrics=['accuracy'])
    print(model.summary())
    return model


if __name__ == "__main__":
    model = RNN_model()
""" Construct the RNN model for deep learning
"""
# ==================RNN 1======================
# import keras
# from keras import regularizers
# from keras.models import Sequential
# from keras.layers import Dense,Activation,Dropout,Bidirectional
# from keras.layers import LSTM,Masking,Embedding
# from keras.optimizers import Adam
#
# def RNN_model():
#     SEG_LENTH = 180
#     model = Sequential()
#     model.add(Masking(mask_value= [0,0,0,0,0,0,0,0,0,0,0,0],\
#              input_shape=(SEG_LENTH, 12)))
#     model.add(Bidirectional(LSTM(128,dropout=0.2, recurrent_dropout=0.2,\
#                   # kernel_regularizer = regularizers.l2(0.1),\
#                    input_shape = (SEG_LENTH, 12),return_sequences = True), merge_mode='concat'))
#     model.add((Bidirectional(LSTM(64,dropout=0.2, recurrent_dropout=0.2,\
#                   # kernel_regularizer = regularizers.l2(0.1),
#                    return_sequences = True), merge_mode='concat')))
#     model.add(LSTM(2))
#     model.add(Activation('softmax'))
#     adam = Adam()
#     model.compile(loss = 'categorical_crossentropy',optimizer = adam,\
#                   metrics = ['accuracy'])
#     print(model.summary())
#     return model
#
# if __name__ == "__main__":
#      model = RNN_model()

""" Construct the RNN model for deep learning
"""
# ==============================RNN 2===========================
# import keras
# from keras import regularizers
# from keras.models import Sequential
# from keras.layers import Dense,Activation,Dropout
# from keras.layers import LSTM,Masking,Embedding
# from keras.optimizers import Adam
#
# def RNN_model():
#     SEG_LENTH = 180
#     model = Sequential()
#     model.add(Masking(mask_value= [0,0,0,0,0,0,0,0,0,0,0,0],\
#              input_shape=(SEG_LENTH, 12)))
#     model.add(LSTM(128,dropout=0.2, recurrent_dropout=0.2,\
#                   # kernel_regularizer = regularizers.l2(0.1),\
#                    input_shape = (SEG_LENTH, 12),return_sequences = True))
#     model.add(LSTM(64,dropout=0.2, recurrent_dropout=0.2,\
#                   # kernel_regularizer = regularizers.l2(0.1),
#                    return_sequences = True))
#     model.add(LSTM(32))
#     model.add(Dropout(0.2))
#     model.add(Dense(16,activation = 'relu'))
#     model.add(Dense(2,activation = 'softmax'))
#     adam = Adam()
#     model.compile(loss = 'categorical_crossentropy',optimizer = adam,\
#                   metrics = ['accuracy'])
#     print(model.summary())
#     return model

# if __name__ == "__main__":
#      model = RNN_model()
