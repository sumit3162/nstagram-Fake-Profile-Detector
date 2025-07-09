import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def preprocess_data(file_path):
    # Load data
    instagram_df = pd.read_csv(file_path)

    # Shuffle the data
    instagram_df = shuffle(instagram_df, random_state=42)

    # Separate features and target
    X = instagram_df.drop(columns=['is_fake'])
    y = instagram_df['is_fake']

    # Print class distribution in training set
    print("Original - Real:", sum(y == 0), "Fake:", sum(y == 1))

    # Scale the features along with the target variable
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Print class distribution in training and testing sets
    print("Training set - Real:", sum(y_train == 0), "Fake:", sum(y_train == 1))
    print("Testing set - Real:", sum(y_test == 0), "Fake:", sum(y_test == 1))

    return X_train, X_test, y_train, y_test

