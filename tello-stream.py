import socket
import cv2


videos = cv2.VideoCapture('udp://@0.0.0.0:11111')


while True:
    try:
        ret, frame = videos.read()
        if ret:
            cv2.imshow('Tello',frame)
            cv2.waitKey(1)

    except Exception as err:
        videos.release()
        cv2.destroyAllWindows()
        print(err)