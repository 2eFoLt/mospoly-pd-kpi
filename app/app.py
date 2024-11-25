from flask import Flask

app = Flask(__name__)
application = app
@app.route("/")
def index():
    return "<p>Hello World1</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)