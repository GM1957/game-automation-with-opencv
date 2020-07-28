import cv2
import numpy as np
import pyautogui

def Press(key):
    pyautogui.press(key)

cap = cv2.VideoCapture(0);

# cv2.namedWindow("Tracking")
# cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
# cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
# cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
# cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # l_h = cv2.getTrackbarPos("LH", "Tracking")
    # l_s = cv2.getTrackbarPos("LS", "Tracking")
    # l_v = cv2.getTrackbarPos("LV", "Tracking")

    # u_h = cv2.getTrackbarPos("UH", "Tracking")
    # u_s = cv2.getTrackbarPos("US", "Tracking")
    # u_v = cv2.getTrackbarPos("UV", "Tracking")

    # l_b = np.array([l_h, l_s, l_v])
    # u_b = np.array([u_h, u_s, u_v])
    
    lowred = np.array([143,80,97])
    highred = np.array([183,255,255])

    mask = cv2.inRange(hsv, lowred, highred)


    cv2.line(frame,(170, 150),(450, 150),(0,0,220),9)
    cv2.line(frame,(170, 330),(450,330),(0,0,220),9)
    cv2.line(frame,(170, 0),(170, 650),(0,0,220),9)
    cv2.line(frame,(450, 0),(450, 650),(0,0,220),9)


    # _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours,hierachy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
    #startpoint, endpoint, color, thickness
 
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))
        if y < 150 and x > 170 and x < 450:
            Press('up')
            break
        if y > 330 and x > 170 and x < 450:
            Press('down')
            break
        if x < 170:
            Press('left')
            break
        if x > 450:
            Press('right')
            break           
        break

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    # cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()