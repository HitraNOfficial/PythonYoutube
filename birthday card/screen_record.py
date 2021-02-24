import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)

filename = 'video.mp4'

codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 24.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Live', 480, 270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert it from BGR ( Blue, Green, Red) to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)
    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
