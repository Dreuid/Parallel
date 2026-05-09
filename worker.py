import json
from google.cloud import pubsub_v1, firestore

PROJECT_ID = "distributing-voting-system"
SUBSCRIPTION_ID = "vote-topic-sub" # [cite: 174]

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)
db = firestore.Client(project=PROJECT_ID)

def process_vote(message): # [cite: 254]
    try:
        # Decode and parse incoming vote message [cite: 255]
        vote = json.loads(message.data.decode("utf-8")) # [cite: 256]
        
        # Enforce idempotent writes [cite: 261]
        doc_id = f"{vote['user_id']}_{vote['poll_id']}" # [cite: 260]
        
        # Store in Firestore [cite: 263]
        db.collection("votes").document(doc_id).set(vote) # [cite: 264]
        
        print(f"Processed vote: {vote['user_id']} | Poll: {vote['poll_id']}") # [cite: 323]
        
        # Confirm message handling [cite: 267]
        message.ack() # [cite: 268]
    except Exception as e:
        print(f"Error processing message: {e}")
        # If an error occurs, the message is not acknowledged [cite: 269]

print("Worker listening for messages...")
streaming_pull_future = subscriber.subscribe(subscription_path, callback=process_vote)

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()