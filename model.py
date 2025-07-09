# model.py

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

def create_model(input_shape, num_classes):
    model = Sequential()
    model.add(Dense(50, input_dim=input_shape, activation='relu'))
    model.add(Dense(150, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(150, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(25, activation='relu'))
    model.add(Dropout(0.3))
    
    # Change the output layer to have as many neurons as classes
    model.add(Dense(num_classes, activation='softmax'))

    return model

def train_model(model, X_train, y_train, epochs):
    # Change the loss to 'sparse_categorical_crossentropy'
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    epochs_hist = model.fit(X_train, y_train, epochs=epochs, verbose=1, validation_split=0.1)

    return epochs_hist
