import cv2

#cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Couldn't open the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read a frame from webcam.")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()