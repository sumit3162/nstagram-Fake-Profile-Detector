import tensorflow as tf

def train_model(model, X_train, y_train, epochs):
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    epochs_hist = model.fit(X_train, y_train, epochs=epochs, verbose=1, validation_split=0.1)

    return epochs_hist
