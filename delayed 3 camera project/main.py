import cv2
import queue
import threading
from camera_thread import read_camera
from camera_viewer import camera_viewer

if __name__ == "__main__":

    print("Starting camera data stream and imaging.")


    camera = cv2.VideoCapture(0)

    warehouse1 = queue.Queue()
    warehouse2 = queue.Queue()
    warehouse3 = queue.Queue()

    thread1 = threading.Thread(target=read_camera, args=(camera, warehouse1, 1))
    thread2 = threading.Thread(target=read_camera, args=(camera, warehouse2, 10))
    thread3 = threading.Thread(target=read_camera, args=(camera, warehouse3, 60))

    thread1.start()
    thread2.start()
    thread3.start()

    viewer1 = threading.Thread(target=camera_viewer, args=(warehouse1, "Camera1"))
    viewer2 = threading.Thread(target=camera_viewer, args=(warehouse2, "Camera2"))
    viewer3 = threading.Thread(target=camera_viewer, args=(warehouse3, "Camera3"))

    viewer1.start()
    viewer2.start()
    viewer3.start()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    thread1.join()
    thread2.join()
    thread3.join()

    viewer1.join()
    viewer2.join()
    viewer3.join()


    camera.release()
    cv2.destroyAllWindows()

    print("The program has ended.")



