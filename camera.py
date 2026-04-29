import cv2 as c
import hand_tracking as ht
import draw

draw_points = []

def startCapture(cam):
    global draw_points
    while True:
        x,frame = cam.read()
        frame = c.flip(frame, 1)
        if not x:
            break

        rgb = c.cvtColor(frame,c.COLOR_BGR2RGB)
        gesture_l,gesture_r,index_pos,draw_points = ht.checkHands(frame,rgb,draw_points)
        draw_points = draw.drawPicture(frame,gesture_l,gesture_r,index_pos,draw_points)

        c.imshow("Hand",frame)

        if c.waitKey(1) == 27:  #esc key
            break

    cam.release()
    c.destroyAllWindows()