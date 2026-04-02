import camera
import cv2 as c

if "__main__":
    cam = c.VideoCapture(0) #default camera on computer
    camera.startCapture(cam)