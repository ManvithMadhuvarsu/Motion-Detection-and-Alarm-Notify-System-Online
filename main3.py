import cv2
import tkinter as tk
from tkinter import filedialog
from twilio.rest import Client
import datetime

# Initialize Twilio client
account_sid = "Your-SID"
auth_token = "Your-Token"
from_number = "Provided-from-number"
to_numbers = ["num-1", "num-2"]
client = Client(account_sid, auth_token)

# Initialize GUI
root = tk.Tk()
root.title('Motion Detection')
root.geometry('300x150')

label = tk.Label(root, text='Select a video file')
label.pack(pady=10)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('Video Files', '*.mp4;*.avi')])
    motion_detection(file_path)

button = tk.Button(root, text='Select File', command=select_file)
button.pack(pady=10)

def motion_detection(file_path):
    cascPath = "Path-of-haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    cap = cv2.VideoCapture(file_path)

    frame_count = 30
    first_frame = None
    buffer_size = 10
    buffer = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        people = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in people:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            screenshot_name = f'screenshot_{frame_count}.png'
            image_path = 'Path-to-save-the-screenshot' + screenshot_name
            cv2.imwrite(image_path, frame)
            # Send SMS notification
            message = client.messages.create(
                body='Motion detected!',
                from_=from_number,
                to=to_numbers,
            )
        
        cv2.namedWindow('Motion Detection', cv2.WINDOW_NORMAL)
        buffer.append(frame)

        if len(buffer) > buffer_size:
            buffer.pop(0)

        if len(buffer) == buffer_size:
            cv2.imshow('Motion Detection', buffer[0])

        if cv2.waitKey(35) == ord('c'):
            break

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

# Run GUI
root.mainloop()
