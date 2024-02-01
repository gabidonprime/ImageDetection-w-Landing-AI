import cv2

cap = cv2.VideoCapture(1)  # Adjust the index as needed

ret, frame = cap.read()
if ret:
    cv2.imshow("Test Frame", frame)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()
else:
    print("Failed to grab frame")

cap.release()