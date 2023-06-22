import cv2

vcap = cv2.VideoCapture("rtsp://admin:Nhat24032002@192.168.1.2/?t=8995918764#live")

while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)