import cv2 as c

def checkDraw(frame,gesture,index_pos,draw_points): 
    x = int(index_pos.x * frame.shape[1])
    y = int(index_pos.y * frame.shape[0])

    if gesture == "one":
        draw_points.append((x, y))
    
    if draw_points:
        for point in draw_points:
            c.circle(frame, point, 5, (0, 255, 0), -1)

    return draw_points

def removeCanvas():
    return []