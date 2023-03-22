# program to capture single image from webcam in python
  
# importing OpenCV library
# import cvui
import cv2
from datetime import datetime
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that

# rtsp_username = "admin"
# rtsp_password = "Hanh.1972"
# width = 800
# height = 480
# cam_no = 1

def create_camera ():
    rtsp = "rtsp://admin:Nhat24032002@192.168.1.2/?t=8995918764#live" 
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    cap.set(3, 1920)  # ID number for width is 3
    cap.set(4, 1080)  # ID number for height is 480
    cap.set(10, 100)  # ID number for brightness is 10qq
    return cap
cam = create_camera()

# cvui.init('screen')
# while True:
#     success, current_cam = cam.read()
#     dim = (width, height)
#     Full_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA)
#     cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
#     cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
#     if (cvui.button(Full_frame, width - 100, height - 40, "Next") and cvui.mouse(cvui.CLICK)):
#         print("Next Button Pressed")
#         cvui.init('screen')
#         cam_no = cam_no+1
#         if (cam_no>4):
#             cam_no=1
#         del cam
#         cam = create_camera(str(cam_no))
#     if (cvui.button(Full_frame, width - 200, height - 40, "Previous") and cvui.mouse(cvui.CLICK)):
#         print("Previous Button Pressed")
#         cvui.init('screen')
#         cam_no = cam_no - 1
#         if (cam_no<1):
#             cam_no=4
#         del cam
#         cam = create_camera(str(cam_no))
#     cv2.imshow('screen', Full_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break


# cam_port = 0
# cam = cv2.VideoCapture(cam_port)
dateTime = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
print(dateTime)
# reading the input using the camera
result, image0 = cam.read()
image = cv2.resize(image0, (1920,1080))

  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    cv2.imshow(dateTime, image)
  
    # saving image in local storage
    cv2.imwrite(dateTime + ".png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    cv2.waitKey(0)
    cv2.destroyWindow(dateTime)
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")