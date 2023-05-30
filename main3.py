import cv2
import tkinter as tk
from tkinter import filedialog
from twilio.rest import Client
import datetime

# Initialize Twilio client
account_sid = "ACf73c6515b5cc4386850bce43258802a0"
auth_token = "a625687e474c62dfd6364711817993f3"
from_number = "+13158093226"
to_numbers = ["+916304322533", "+919491592005"]
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
    cascPath = "D:\\Mini Project\\Coding\\harcascade\\haarcascade_frontalface_default.xml"
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
            image_path = 'D:\\Mini Project\\Coding\\Recordings\\Recorded' + screenshot_name
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
