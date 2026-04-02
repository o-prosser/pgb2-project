import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands = 1)
mp_draw = mp.solution.drawing_utils

def checkHands(frame,rgb):
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)


