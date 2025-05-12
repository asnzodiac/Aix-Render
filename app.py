from flask import Flask, render_template, jsonify
from scrape import get_flight_times

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/times/<flight_no>")
def api_times(flight_no):
    return jsonify(get_flight_times(flight_no))

if __name__ == "__main__":
    app.run(debug=True)
