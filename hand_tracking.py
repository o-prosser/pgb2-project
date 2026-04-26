import mediapipe as mp
import keyboard
import csv

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

def checkHands(frame, rgb,frame_width,frame_height):

    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            label = handedness.classification[0].label
            if label == "Left" and keyboard.is_pressed("1"):
                hand_landmarks_list = getHandData(landmarks, frame_width, frame_height)
                addHandData(hand_landmarks_list)


def getHandData(hand_landmarks,frame_width,frame_height):
    hand_landmarks_list=[]
    for lm in hand_landmarks.landmark:
        hand_landmarks_list.extend([lm.x,lm.y,lm.z])

    return hand_landmarks_list

def addHandData(hand_landmarks_list):
    print("scanning!!!!")
    with open("hand_recognition_data.csv","a",newline="") as file:
        hand_writer = csv.writer(file)
        hand_writer.writerow(["lead"] + hand_landmarks_list)
