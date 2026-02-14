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

