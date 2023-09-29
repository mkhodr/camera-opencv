import numpy as np
import cv2 as cv
import requests
from keys import user, password, ipport

def get_feed(cam=0, stream=0):
    stream_url = f'rtsp://{user}:{password}@{ipport}/cam/realmonitor?channel={cam}&subtype={stream}'
    cap = cv.VideoCapture(stream_url)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Process the video frame here

        cv.imshow('Camera Stream', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

get_feed(2)