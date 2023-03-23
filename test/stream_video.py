import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer

app = QApplication([])
window = QWidget()
window.setWindowTitle("IP Camera Stream")

video_label = QLabel()
video_label.setAlignment(Qt.AlignCenter)

layout = QVBoxLayout()
layout.addWidget(video_label)
window.setLayout(layout)
window.showMaximized()

cap = cv2.VideoCapture("rtsp://admin:Nhat24032002@192.168.1.2/?t=8995918764#live")

def update_video_stream():
    ret, frame = cap.read()
    if ret:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(image, image.shape[1], image.shape[0], QImage.Format_RGB888)
        video_label.setPixmap(QPixmap.fromImage(image))

timer = QTimer()
timer.timeout.connect(update_video_stream)
timer.start(30)

app.exec_()