import cv2 as c
import numpy as n

col = (0, 255, 0)

def handleDraw(frame, gesture_l, gesture_r, index_pos, draw_points):
    global col

    x = int(index_pos.x * frame.shape[1])
    y = int(index_pos.y * frame.shape[0])

    if gesture_l == "one":
        if gesture_r == "one":
            draw_points.append([(x, y),col])

    if gesture_l == "zero" and gesture_r == "open":
        return removeCanvas()
    
    if draw_points:
        for point in draw_points:
            c.circle(frame, point[0], 5, point[1], -1)

    return draw_points

def removeCanvas():
    return []