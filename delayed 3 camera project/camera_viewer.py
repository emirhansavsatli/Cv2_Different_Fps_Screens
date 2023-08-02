import cv2
import queue

def camera_viewer(warehouse, window_name):
    while True:
        try:
            frame = warehouse.get_nowait()

            if frame is not None:
                cv2.imshow(window_name, frame)
        except queue.Empty:
            print("ERROR")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


