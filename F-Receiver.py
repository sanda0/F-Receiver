from flask import Flask,request
import socket

import os

banner = '''
 _____         ____                     _
|  ___|       |  _ \   ___   ___   ___ (_)__   __  ___  _ __
| |_    _____ | |_) | / _ \ / __| / _ \| |\ \ / / / _ \| '__|
|  _|  |_____||  _ < |  __/| (__ |  __/| | \ V / |  __/| |
|_|           |_| \_\ \___| \___| \___||_|  \_/   \___||_|
by sandakelum priyamantha
'''
print(banner)

def get_ip():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    return s.getsockname()[0]

def create_page(fname):
    if fname != "":
        txt = "<p>%s is uploaded!</p>"%(fname)
    else:
        txt = ""
    
    page_html = '''
    <html>
    <title>F-Receiver</title>
    <body>
        <h3>F-Receiver</h3>
        <p>select file and upload!</p>
        <form action="" method="post" enctype="multipart/form-data">
            <p><input type="file" name="file"/></p>
            <p><input type="submit"/></p>
        </form>
        %s
        <p>&copy sandakelum priyamantha</p>
    </body>
    </html>
    '''%(txt)
    return page_html

port = 501
ipaddr = get_ip()

app = Flask(__name__)

UPLOAD_FOLDER = ""
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename

        if filename != "":
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return create_page(filename)
    return create_page("")

if __name__ == '__main__':
    app.run(debug=False,host=ipaddr,port=port)
