import concurrent.futures
import threading

# Define four independent deduction functions [cite: 66]
def compute_sss(salary):
    print(f"[Task] Computing SSS on {threading.current_thread().name}")
    return salary * 0.045  # 4.5% [cite: 16]

def compute_philhealth(salary):
    print(f"[Task] Computing PhilHealth on {threading.current_thread().name}")
    return salary * 0.025  # 2.5% [cite: 17]

def compute_pagibig(salary):
    print(f"[Task] Computing Pag-IBIG on {threading.current_thread().name}")
    return salary * 0.02   # 2.0% [cite: 18]

def compute_tax(salary):
    print(f"[Task] Computing Tax on {threading.current_thread().name}")
    return salary * 0.10   # 10.0% [cite: 19]

def run_task_parallelism():
    employee_name = "Alice"
    salary = 25000
    
    # Use ThreadPoolExecutor to run them concurrently [cite: 67]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Retrieve results using Future objects [cite: 68]
        f_sss = executor.submit(compute_sss, salary)
        f_ph = executor.submit(compute_philhealth, salary)
        f_ibig = executor.submit(compute_pagibig, salary)
        f_tax = executor.submit(compute_tax, salary)
        
        # Collecting all partial results [cite: 69]
        sss = f_sss.result()
        philhealth = f_ph.result()
        pagibig = f_ibig.result()
        tax = f_tax.result()
        
    total_deduction = sss + philhealth + pagibig + tax
    
    print(f"\n--- Payroll for {employee_name} ---")
    print(f"SSS: {sss:.2f}")
    print(f"PhilHealth: {philhealth:.2f}")
    print(f"Pag-IBIG: {pagibig:.2f}")
    print(f"Tax: {tax:.2f}")
    print(f"Total Deduction: {total_deduction:.2f}") # [cite: 71]

if __name__ == "__main__":
    run_task_parallelism()