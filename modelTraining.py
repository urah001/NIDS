import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# the train data
train=pd.read_csv('https://raw.githubusercontent.com/urah001/wiresharkDataset/refs/heads/main/Train_data.csv')
#the test data
test=pd.read_csv('https://raw.githubusercontent.com/urah001/wiresharkDataset/refs/heads/main/custech_test_data.csv')

# Features and labels
X = train.drop(columns=["label"])  # Features
y = train["label"]  # Labels: 0 = normal, 1 = intrusion


# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "model.joblib")