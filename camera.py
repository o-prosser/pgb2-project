import cv2 as c
import hand_tracking as ht

def startCapture(cam):
    while True:
        x,frame = cam.read()
        if not x:
            break

        rgb = c.cvtColor(frame,c.COLOR_BGR2RGB)
        ht.checkHands(frame,rgb)

        c.imshow("Hand",frame)

        if c.waitKey(1) == 27:  #esc key
            break

    cam.release()
    c.destroyAllWindows()