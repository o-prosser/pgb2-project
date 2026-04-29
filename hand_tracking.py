import mediapipe as mp
import keyboard
import csv
import pickle
import pandas as p
import cv2 as c
import draw

with open("gesture_model_left.pkl", "rb") as file:
    hand_model_left = pickle.load(file)

with open("gesture_model_right.pkl", "rb") as file:
    hand_model_right = pickle.load(file)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

draw_points = []

def checkHands(frame, rgb):
    global draw_points

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            handedness = handedness.classification[0].label

            hand_landmarks_list = getHandData(landmarks)

            if handedness == "Left":
                if keyboard.is_pressed("1"):
                # if keyboard.is_pressed(18):
                    addHandData(hand_landmarks_list,handedness)
    
                gesture_l = displayCurrentGesture(hand_landmarks_list,frame,handedness)

                if gesture_l == "zero":
                    draw_points = draw.removeCanvas()

            if handedness == "Right":
                if keyboard.is_pressed("2"):
                # if keyboard.is_pressed(19):
                    addHandData(hand_landmarks_list,handedness)
    
                gesture_r = displayCurrentGesture(hand_landmarks_list,frame,handedness)

                draw_points = draw.checkDraw(frame,gesture_r,landmarks.landmark[8],draw_points)
                


def getHandData(hand_landmarks):
    hand_landmarks_list=[]
    for lm in hand_landmarks.landmark:
        hand_landmarks_list.extend([lm.x,lm.y,lm.z])

    return hand_landmarks_list

def addHandData(hand_landmarks_list,handedness):
    print("scanning!!!!")
    with open(f"hand_landmark_data_{handedness.lower()}.csv","a",newline="") as file:
        hand_writer = csv.writer(file)
        hand_writer.writerow(["open"] + hand_landmarks_list)

def displayCurrentGesture(hand_landmarks_list,frame,handedness = "Left"):
    landmarks_df = p.DataFrame([hand_landmarks_list])

    if handedness == "Left":
        prediction = hand_model_left.predict(landmarks_df)
        gesture = prediction[0]
        c.putText(frame, f'Gesture: {gesture}', (10, 30), c.FONT_HERSHEY_SIMPLEX, 1, (29,29,148), 2)
    else:
        prediction = hand_model_right.predict(landmarks_df)
        gesture = prediction[0]
        c.putText(frame, f'Gesture: {gesture}', (10, 60), c.FONT_HERSHEY_SIMPLEX, 1, (29,29,148), 2)

    return gesture