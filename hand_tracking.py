import mediapipe as mp
import keyboard
import csv
import pickle
import pandas as p
import cv2 as c

with open("gesture_model.pkl", "rb") as file:
    hand_model = pickle.load(file)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

def checkHands(frame, rgb):

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            label = handedness.classification[0].label

            hand_landmarks_list = getHandData(landmarks)

            if label == "Left":
                if keyboard.is_pressed("1"):
                # if label == "Left" and keyboard.is_pressed(18):
                    addHandData(hand_landmarks_list)
    
                displayCurrentGesture(hand_landmarks_list,frame)


def getHandData(hand_landmarks):
    hand_landmarks_list=[]
    for lm in hand_landmarks.landmark:
        hand_landmarks_list.extend([lm.x,lm.y,lm.z])

    return hand_landmarks_list

def addHandData(hand_landmarks_list):
    print("scanning!!!!")
    with open("hand_landmark_data.csv","a",newline="") as file:
        hand_writer = csv.writer(file)
        hand_writer.writerow(["zero"] + hand_landmarks_list)

def displayCurrentGesture(hand_landmarks_list,frame):
    landmarks_df = p.DataFrame([hand_landmarks_list])

    prediction = hand_model.predict(landmarks_df)
    gesture = prediction[0]

    c.putText(frame, f'Gesture: {gesture}', (10, 30), c.FONT_HERSHEY_SIMPLEX, 1, (29,29,148), 2)