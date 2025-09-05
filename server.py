from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/reserve", methods=["POST"])
def reserve_ticket():
    data = request.get_json()
    user_id = data.get("user_id")
    name = data.get("name")
    movie = data.get("movie")
    time = data.get("time")

    # برای تست: فقط برگردون
    message = f"✅ {name} عزیز، بلیط فیلم «{movie}» در سانس {time} برای شما رزرو شد!"
    return jsonify({"message": message})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
