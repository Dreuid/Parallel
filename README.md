# Distributed Voting System with Edge-Cloud Architecture

Lorenz Lacanaria (Dreuid)
Nash Andrew Bondoc (nathanjargon)
Kyle Martin Sarmiento (slimetamer1)
James Henry Emorricha (j4mesh3nry)

## 📖 Project Overview
This project implements a highly available, fault-tolerant distributed voting system using Google Cloud Platform (GCP). It leverages an Edge-Cloud architecture to handle high-throughput, concurrent synthetic voting data, buffer it through a messaging queue, and process it idempotently to ensure zero dropped requests and no duplicate votes.

## 🚀 Live Endpoints & Execution
* **Cloud Run API URL:** `https://voting-api-772468966232.asia-southeast1.run.app`
* **Execution Proof:**
<img width="400" height="225" alt="PDC SECOND GROUP ACT" src="https://github.com/user-attachments/assets/b4541f1b-f8de-4e09-93ba-4b3d0b99c400" />

  *(Watch the system process concurrent edge node traffic, buffer through Pub/Sub, and write to Firestore in real-time).*



## ⚙️ System Architecture

1. **Edge Nodes (`edge_node.py`)**: Simulates distributed users casting votes. Generates a high volume of concurrent HTTP POST requests with randomized choices and unique UUIDs.
2. **Cloud API (`api.py`)**: A Flask web service deployed on GCP Cloud Run. Acts as the ingestion point, receiving votes and immediately publishing them to a messaging queue to prevent dropped requests during extreme traffic spikes.
3. **Message Queue (GCP Pub/Sub)**: The `vote-topic` receives data from the API and queues it in the `vote-sub` subscription. This completely decouples the public-facing web server from the backend database operations.
4. **Background Worker (`worker.py`)**: An asynchronous Python service that acts as a subscriber. It continuously pulls batches of messages from Pub/Sub, processes the payload, and commits them to the database.
5. **Database (GCP Firestore)**: A NoSQL document database. To guarantee **fault tolerance** and **idempotency**, the worker assigns a composite Document ID (`user_id_poll_id`). If Pub/Sub accidentally delivers the same vote twice, Firestore simply overwrites the exact same data, preventing duplicate votes from being counted.

---

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Web Framework:** Flask
* **Cloud Provider:** Google Cloud Platform (GCP)
* **Infrastructure Services:** Cloud Run, Cloud Pub/Sub, Firestore

---

## 💻 Local Setup & Testing

### Prerequisites
1. Ensure Python 3+ is installed.
2. Install the Google Cloud CLI (`gcloud`).
3. Authenticate your machine:
   ```bash
   gcloud auth application-default login


   
