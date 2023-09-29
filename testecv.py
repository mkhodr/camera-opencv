import numpy as np
import cv2 as cv
import requests
from keys import user, password, ipport

stream_url = f'rtsp://{user}:{password}@{ipport}/cam/realmonitor?channel=2&subtype=0'

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