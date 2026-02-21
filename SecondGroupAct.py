import time
import concurrent.futures

# Simulate the time it takes to play one match (e.g., 0.2 seconds for our simulation)
# In real life, this would be ~15-20 minutes!
MATCH_DURATION = 0.2

# Number of parallel setups (consoles/monitors) available
NUM_SETUPS = 4

# The distribution of our 24 matches across the 5 rounds of a 25-person bracket
tournament_rounds = [9, 8, 4, 2, 1]

def play_match(match_id):
"""
Simulates a single tournament match.
This is our 'Work Unit'.
"""
time.sleep(MATCH_DURATION)
return f"Match {match_id} completed"

def run_sequential():
"""Simulates the 1-setup bottleneck."""
print("--- Starting Sequential Tournament (1 Setup) ---")
start_time = time.time()

match_counter = 1
for round_num, num_matches in enumerate(tournament_rounds, 1):
print(f" Running Round {round_num} ({num_matches} matches)...")
for _ in range(num_matches):
play_match(match_counter)
match_counter += 1

end_time = time.time()
return end_time - start_time

def run_parallel():
"""Simulates a multi-setup tournament using Data Parallelism."""
print(f"\n--- Starting Parallel Tournament ({NUM_SETUPS} Setups) ---")
start_time = time.time()

match_counter = 1