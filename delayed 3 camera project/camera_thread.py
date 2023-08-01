import time
import cv2
import threading
import queue

def read_camera(camera, warehouse, fps):
    slowness = 1 / fps

    while True:
        ret, frame = camera.read()
        if ret:
            warehouse.put(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(slowness)

    camera.release()
