import threading
import multiprocessing
import time

def compute_gwa(grades, mode="Thread"):
    """
    a slight delay to mimic processing time, 
    then calculates and prints GWA.
    """
    time.sleep(0.1) 
    gwa = sum(grades) / len(grades) if grades else 0
    print(f"[{mode}] Output: {gwa:.2f}")
    
    def get_user_inputs():
        print("--- Grade Input System ---")
    try:
        raw_input = input("Enter grades separated by spaces (e.g., 85 90 78): ")
        return [float(g) for g in raw_input.split()]
    except ValueError:
        print("Invalid input. Using default values.")
        return [85, 90, 78, 92]

def run_experiment(method_type, grades):
    start_time = time.perf_counter()
    workers = []
    
    # We treat each grade as a 'subject' to process independently as per instructions
    for g in grades:
        if method_type == "Multithreading":
            worker = threading.Thread(target=compute_gwa, args=([g], "Thread"))
        else:
            worker = multiprocessing.Process(target=compute_gwa, args=([g], "Process"))
        
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()
        
    end_time = time.perf_counter()
    return end_time - start_time

if name == "main":
    user_grades = get_user_inputs()

    #Run Multithreading
    print("\nStarting Multithreading...")
    thread_time = run_experiment("Multithreading", user_grades)
    
    print("\nStarting Multiprocessing...")
    process_time = run_experiment("Multiprocessing", user_grades)

    print(f"\n--- Results ---")
    print(f"Threading Time: {thread_time:.4f}s")
    print(f"Processing Time: {process_time:.4f}s")