from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def index():
    args = request.args


    vastaus = {

    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='localhost', port=3000)