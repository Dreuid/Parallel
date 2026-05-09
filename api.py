print("1. File is executing...")
from flask import Flask, request, jsonify
from google.cloud import pubsub_v1

print("2. Imports successful...")
app = Flask(__name__)

# Make sure this has your actual Project ID!
PROJECT_ID = "distributing-voting-system" 
TOPIC_ID = "vote-topic"

print("3. Connecting to Google Cloud Pub/Sub...")
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route("/vote", methods=["POST"])
def receive_vote():
    vote = request.get_json()
    if not vote or 'user_id' not in vote or 'poll_id' not in vote:
        return jsonify({"error": "Invalid payload"}), 400
    try:
        import json
        data = json.dumps(vote).encode("utf-8")
        publisher.publish(topic_path, data)
        return jsonify({"status": "accepted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

print("4. Reached the bottom block...")

if __name__ == "__main__":
    print("5. Attempting to start Flask server on port 8080...")
    app.run(host="0.0.0.0", port=8080)