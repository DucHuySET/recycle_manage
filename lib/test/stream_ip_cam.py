import cv2 
import time
def main(args):
    #cap = cv2.VideoCapture(0) #default camera
    cap = cv2.VideoCapture('rtsp://admin:Ctarg_123@192.168.1.100') #IP Camera
    
    while(True):
        try:
            ret, frame = cap.read()
            frame=cv2.resize(frame, (600, 600)) 
            cv2.imshow('Capturing',frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'): #click q to stop capturing
                break
        except Exception:
            print("loading")
        time.sleep(0.1)
    cap.release()
    cv2.destroyAllWindows()
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
