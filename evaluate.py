import numpy as np
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def evaluate_model(model, X_test, y_test):
    y_pred = np.argmax(model.predict(X_test), axis=1)
    y_true = np.array(y_test)

    accuracy = accuracy_score(y_true, y_pred)
    confusion_mat = confusion_matrix(y_true, y_pred)
    class_report = classification_report(y_true, y_pred)

    return accuracy, confusion_mat, class_report
