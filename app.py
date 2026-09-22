from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
KEYWORDS={"kheti":"agriculture","dudh":"diary","silai":"tailoring","computer":"it"}
def find_sector(text):
    for word,sector in KEYWORDS.items():
        if word in text.lower():
            return sector
        return None
@app.route("/")
def home():
    return "Setup ho gya!"
if __name__ == "__main__":
    app.run(debug=True)
