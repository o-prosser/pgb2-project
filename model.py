import pandas as p
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# from sklearn.ensemble import VotingClassifier

for hand in [["left","Paint"],["right","Brush"]]:
        landmark_df = p.read_csv("hand_landmark_data_"+ hand[0] +".csv")

        X = landmark_df.drop(hand[1], axis=1)
        Y = landmark_df[hand[1]]

        X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2,random_state=42)

        knn = KNeighborsClassifier(n_neighbors = 5)

        knn.fit(X_train,Y_train)

        y_pred = knn.predict(X_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

        with open("gesture_model_"+ hand[0] +".pkl","wb") as file:
                pickle.dump(knn,file)
