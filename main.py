import cv2
import pyautogui
import datetime
import time
from twilio.rest import Client
#Twilio Account Details
account_sid = "ACf73c6515b5cc4386850bce43258802a0"
auth_token = "a625687e474c62dfd6364711817993f3"
from_number = "+13158093226"
to_numbers = ["+916304322533", "+919491592005"]
client = Client(account_sid, auth_token)

path = "D:\\Mini Project\\Coding\\harcascade\\haarcascade_upperbody.xml"
cascade = cv2.CascadeClassifier(path)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 15)


duration = 20
interval = 2
screenshot_num = 1

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_name = f"D:\\Mini Project\\Coding\\Recordings\\Real Time\\Videos\\video_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4v"
out = cv2.VideoWriter(video_name, fourcc, 10.0, (640, 480))

start_time = time.time()
end_time = start_time + duration

while time.time() < end_time:
    ret, image = cap.read()
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    upperbody = cascade.detectMultiScale(gray_scale, 1.2, 4)

    for x, y, w, h in upperbody:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        client.messages.create(
            body="Movement detected!",
            from_=from_number,
            to=to_numbers,
        )

    out.write(image)

    if time.time() - start_time >= interval * screenshot_num:
        screenshot = pyautogui.screenshot()
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
        image_path = f'D:\\Mini Project\\coding\\Recordings\\Real Time\\Screenshots\\screenshot_{timestamp}.png'
        screenshot.save(image_path)
        screenshot_num += 1
        print(f'Screenshot {screenshot_num-1} taken')

    cv2.imshow("Frame", image)
    if cv2.waitKey(1) & 0xFF == ord("c"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
