from preprocess import preprocess_data
from model import create_model
from train import train_model
from evaluate import evaluate_model
from interpret import visualize_confusion_matrix

# Step 1: Preprocessing
X_train, X_test, y_train, y_test = preprocess_data('instagram_data.csv')

# Step 2: Create Model

num_classes = 2  # Set the number of classes
model = create_model(input_shape=X_train.shape[1], num_classes=num_classes)


# Step 3: Train Model
epochs_hist = train_model(model, X_train, y_train, epochs=50)

# Step 4: Evaluate Model
accuracy, confusion_mat, class_report = evaluate_model(model, X_test, y_test)

# Step 5: Interpretation
visualize_confusion_matrix(confusion_mat)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{class_report}')
