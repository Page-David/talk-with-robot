from flask import Flask,request,render_template
import requests,urllib.parse

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home2():
    #print(request.method)
    if request.method=='POST':
        text=urllib.parse.quote(request.form['text'])
        url='http://www.tuling123.com/openapi/api?key=4b130e3d0fa202cb8499327de4ce0bcc&info='
        url=url+text
        r = requests.get(url)
        return render_template("home2.html",retext=r.json()['text'])
    else:
        return render_template("home2.html")

if __name__=='__main__':
    app.run()
