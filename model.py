import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

landmark_df = p.read_csv("hand_landmark_data.csv")

X = landmark_df.drop('lead', axis=1)
y = landmark_df['lead']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)
