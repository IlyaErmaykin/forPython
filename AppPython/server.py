from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    val = "W(O_o)w";
    helloVal = "Hello World!";
    res = (helloVal + val);
    return  res;

if __name__ == "__main__":
    app.run()
