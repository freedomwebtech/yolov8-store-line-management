import cv2    
import time
cpt = 0
maxFrames = 580 # if you want 5 frames only.


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        point = [x, y]
        print(point)
  
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap=cv2.VideoCapture(r'C:\Users\freed\Videos\headcountnew.avi')
area=[(422,78),(422,435),(691,436),(702,37)]
while cpt < maxFrames:
    ret, frame = cap.read()
    if not ret:
        break
    frame=cv2.resize(frame,(1020,500))
    cv2.imshow("RGB", frame) # show image in window
    cv2.imwrite(r'C:\Users\freed\Downloads\yolov8-custom-object-main\yolov8-custom-object-main\images\personhead_%d.jpg' %cpt, frame)
    cpt += 1
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()