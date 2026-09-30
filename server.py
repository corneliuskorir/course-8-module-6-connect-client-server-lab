from flask import Flask, jsonify, request
from flask_cors import CORS

from data import events

app = Flask(__name__)
CORS(app)


@app.route("/")
def welcome():
    return jsonify({"message": "Welcome"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()
    if "title" in data:
        new_id = max((e["id"] for e in events), default=0) + 1
        new_event = {"id": new_id, "title": data["title"]}
        events.append(new_event)
        return jsonify(new_event), 201
    return jsonify({"error": 'missing argument "title"'}), 400


# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201

if __name__ == "__main__":
    app.run(debug=True)
