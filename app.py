from flask import Flask, render_template, request, url_for
import subprocess
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('home4.html')
@app.route('/start_tracking', methods=['POST'])
def start_tracking():
    if request.method == 'POST':
        subprocess.Popen(["python", "D:\\Mini Project\\coding\\main.py"])
    return "Tracking started!"

@app.route('/start_executing', methods=['POST'])
def start_executing():
    if request.method == 'POST':
        subprocess.Popen(["python", "D:\\Mini Project\\coding\\main3.py"])
    return "Tracking started!"
if __name__ == '__main__':
    app.run(debug=True)

