from flask import Flask

app = Flask(__name__)

# Compliance violation: hardcoded secret
API_KEY = "12345-SECRET-KEY"

@app.route("/")
def home():
    return "Secure App Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)