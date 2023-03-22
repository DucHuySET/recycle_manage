import cv2 
def main(args):
    #cap = cv2.VideoCapture(0) #default camera
    cap = cv2.VideoCapture('rtsp://admin:Nhat24032002@192.168.1.2/?t=8995918764#live') #IP Camera
    
    while(True):
        ret, frame = cap.read()
        frame=cv2.resize(frame, (960, 540)) 
        cv2.imshow('Capturing',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): #click q to stop capturing
            break
    cap.release()
    cv2.destroyAllWindows()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))