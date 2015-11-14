from flask import Flask,request,render_template
import requests,urllib.parse
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def robot():
    if request.method == "POST":
        text=urllib.parse.quote(request.form['text'])
        url='http://www.tuling123.com/openapi/api?key=4b130e3d0fa202cb8499327de4ce0bcc&info='
        url+=text
        r=requests.get(url)
        print('User send a click,json data is ',r.json())
        if  r.json()['code'] == 100000:
            return render_template('robot.html',retext=r.json()['text'])
        elif r.json()['code'] == 302000:
            return render_template('robot.html',retext=r.json()['text'],list=r.json()['list'])
        elif r.json()['code'] == 200000:
            return render_template('robot.html',retext=r.json()['text'],reurl=[r.json()['url'],request.form['text']])
        elif r.json()['code'] == 305000:
            return render_template('robot.html',retext=r.json()['text'],retrain=r.json()['list'])
        elif r.json()['code'] == 306000:
            return render_template('robot.html',retext=r.json()['text'],replane=r.json()['list'])
        elif r.json()['code'] == 308000:
            return render_template('robot.html',retext=r.json()['text'],redish=enumerate(r.json()['list']))
    else:
        return render_template('robot.html')

if __name__=='__main__':
    app.run()

