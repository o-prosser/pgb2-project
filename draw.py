import cv2 as c
import numpy as n
import random

col = (0, 255, 0)
pen_size = 5
mode = "normal"

def handleDraw(frame, gesture_l, gesture_r, index_pos, draw_points):
    global col,pen_size,mode

    x = int(index_pos.x * frame.shape[1])
    y = int(index_pos.y * frame.shape[0])

    picker_range = 0.75 * frame.shape[0]

    if gesture_l == "Paint": #paintbrush
        if gesture_r == "Brush":
            draw_points.append([(x, y),pen_size,col])

    if gesture_l == "Rubber": #rubber
        draw_points = draw_points.copy()

        for point in draw_points:
            if abs(point[0][0] - x) < 10 and abs(point[0][1] -y) < 10:
                draw_points.remove(point)

    if gesture_l == "Colour": #colour
        hue = int((y / picker_range) * 179)
        hsv_col = n.uint8([[[hue, 255, 255]]])
        bgr_col = c.cvtColor(hsv_col, c.COLOR_HSV2BGR)
        col = tuple(int(z) for z in bgr_col[0][0])

        if 0 < y < 40:
            c.circle(frame, (x - 40,y + 40), pen_size, col, -1)
        else:
            c.circle(frame, (x - 40,y - 40), pen_size, col, -1)

    if gesture_l == "Size": #size
        pen_size = max(1,int((1 - (y/picker_range)) * 12) + 1)

        if 0 < y < 40:
            c.circle(frame, (x - 40,y + 40), pen_size, col, -1)
        else:
            c.circle(frame, (x - 40,y - 40), pen_size, col, -1)

    if gesture_l == "Mode": #mode
        if 0 < y < 0.33 *(frame.shape[0]):
            mode = "normal"
            c.putText(frame, f'Normal', (x - 40,y + 40), c.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        elif 0.33 * (frame.shape[0]) < y < 0.66 * (frame.shape[0]):
            mode = "spray"
            c.putText(frame, f'Spray', (x -40,y + 40), c.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        else:
            mode = "mirror"
            c.putText(frame, f'Mirror', (x - 40,y + 40), c.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    if gesture_l == "Erase" and gesture_r == "Open":
        return removeCanvas()
    
    return draw_points
    
def drawPicture(frame,gesture_l,gesture_r,index_pos,draw_points):

    for point in draw_points:
        c.circle(frame, point[0], point[1], point[2], -1)

    if index_pos is None:
        return draw_points

    x = int(index_pos.x * frame.shape[1])
    y = int(index_pos.y * frame.shape[0])
        
    spray = []
        
    if mode == "spray" and gesture_l == "Paint" and gesture_r == "Brush":
        for i in range(10):
                rand_x = x + random.randint(-20,20)
                rand_y = y + random.randint(-20,20)
                c.circle(frame, (rand_x,rand_y), 2, col, -1)
                spray.append([(rand_x,rand_y),2,col])
        draw_points.extend(spray)

    if mode == "mirror" and gesture_l == "Paint" and gesture_r == "Brush":
        mirror_x = frame.shape[1] - x
        c.circle(frame,(mirror_x,y),pen_size,col,-1)
        draw_points.append([(mirror_x, y),pen_size,col])

    return draw_points

def removeCanvas():
    return []