import cv2
vidCap = cv2.VideoCapture(0)
while True:
    ret , video = vidCap.read()
    cv2.imshow("video_live", video)
    if cv2.waitKey(10) == ord("a"):
        break;
vidCap.release()