import time
import random
import uuid
import requests #

API_URL = "http://127.0.0.1:8080/vote" # Will be updated once deployed

def generate_vote():
    # Extend to simulate multiple edge nodes [cite: 191]
    return {
        "user_id": str(uuid.uuid4()), # [cite: 194]
        "poll_id": "poll_1", # [cite: 196]
        "choice": random.choice(["A", "B", "C"]), # [cite: 197]
        "timestamp": time.time() # [cite: 197]
    }

def send_vote(vote):
    # Implement retry logic and simulate network instability [cite: 203, 204]
    try:
        response = requests.post(API_URL, json=vote) # [cite: 206]
        print(f"Vote generated: {vote['user_id']} | Choice: {vote['choice']}") # [cite: 321]
    except Exception as e:
        print("Transmission failed:", e) # [cite: 207]

def run_edge_node():
    # Add randomness to simulate real-world edge behavior [cite: 214]
    while True: # [cite: 216]
        vote = generate_vote() # [cite: 217]
        send_vote(vote) # [cite: 218]
        time.sleep(random.uniform(1, 3)) # [cite: 219]

if __name__ == "__main__":
    run_edge_node()