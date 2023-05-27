import cv2 as cv

camera = cv.VideoCapture(1, cv.CAP_DSHOW)
camera.set(cv.CAP_PROP_SETTINGS, 1)
while camera.isOpened():
    _, frame = camera.read()
    cv.imshow("Hasil", frame)
    if cv.waitKey(24) & 0xFF == ord('x'):
        break

camera.release()
cv.destroyAllWindows()