from flask import Flask, render_template
import os;

app = Flask(__name__)

@app.route("/")
def hello():
    val = "W(O_o)w";
    helloVal = "Hello World!";
    res = (helloVal + val);
    return  res;

@app.route('/index')
def index():
    return render_template('index.html');

if __name__ == "__main__":
    app.run()


    #def hello():
#    val = "W(O_o)w";
#    helloVal = "Hello World!";
#    res = (helloVal + val);
#    return  res;