import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Try to get the first frame
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Get the FPS of the camera
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per Second: {fps}")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()