# Motion Detection and Security Notify System

The Motion Detection and Security Notify System is a project aimed at automating the process of motion detection, capturing screenshots, and recording videos when motion is detected in a given area. It utilizes computer vision and machine learning techniques to detect motion and a camera module to capture visual data. The system is designed to enhance security and automation in various applications, including surveillance, security, and home automation.

## Features

- Real-time motion detection: The system uses computer vision algorithms to detect motion in real-time.
- Screenshot capture: When motion is detected, the system captures screenshots of the area of interest.
- Video recording: The system records videos when motion is detected, providing a visual record of the event.
- Web-based interface: The system includes a user-friendly web-based interface to access the captured data and control the system remotely.
- SMS alert notification: Integrated with the Twilio API, the system can send SMS notifications to a provided phone number when motion is detected.

## Requirements

- Python 3.x
- OpenCV
- Flask
- Twilio API credentials

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Configure the Twilio API credentials by providing your account SID, auth token, and the phone number to send the SMS alerts.
4. Run the application using the following command:
   ```
   python app.py
   ```
5. Access the system through the web-based interface by navigating to `http://localhost:5000` in your web browser.

## Usage

1. Click on the "Start Tracking" button to initiate the motion detection process. The system will begin capturing screenshots and recording videos when motion is detected.
2. To select a video from your device for motion detection, click on the "Select Video" button. The system will analyze the selected video for motion and perform the necessary actions.
3. Use the web-based interface to view the captured screenshots and recorded videos. You can also control the system remotely and access other functionalities.

## Contributions

Contributions to the Motion Detection and Security Notify System project are welcome. If you encounter any issues, feel free to open an issue in the repository or submit a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to acknowledge the contributions of the open-source community and the developers of the libraries and tools used in this project. Their efforts have made this project possible.

For any further questions or inquiries, please contact the project maintainer at start3kstark@gmail.com.

Thank you for your interest in the Motion Detection and Security Notify System!
