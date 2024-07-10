from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("hello world")
    return 'Hello, Binod Welcome!!!!!'
    print("Hello Binod")

if __name__ == '__main__':
    app.run(debug=True)
