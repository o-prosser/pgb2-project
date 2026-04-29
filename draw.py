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

    if gesture_l == "two":
        draw_points = draw_points.copy()

        for point in draw_points:
            if abs(point[0][0] - x) < 10 and abs(point[0][1] -y) < 10:
                draw_points.remove(point)

    if gesture_l == "three":

        hue = int(index_pos.x * 179)
        hsv_col = n.uint8([[[hue, 255, 255]]])
        bgr_col = c.cvtColor(hsv_col, c.COLOR_HSV2BGR)
        col = tuple(int(x) for x in bgr_col[0][0])

        c.circle(frame, (x,y), 5, col, -1)

    if gesture_l == "zero" and gesture_r == "open":
        return removeCanvas()
    
    if draw_points:
        for point in draw_points:
            c.circle(frame, point[0], 5, point[1], -1)

    return draw_points

def removeCanvas():
    return []