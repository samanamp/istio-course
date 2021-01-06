from flask import Flask
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get('https://www.google.com')
    return str(r.status_code)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)
