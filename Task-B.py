import concurrent.futures
import os

# Single function that performs the complete payroll computation [cite: 76]
def compute_full_payroll(employee):
    name, salary = employee
    # Individual deductions [cite: 77]
    sss = salary * 0.045
    ph = salary * 0.025
    ibig = salary * 0.02
    tax = salary * 0.10
    
    total_deduction = sss + ph + ibig + tax # [cite: 78]
    net_salary = salary - total_deduction # [cite: 79]
    
    # Optional: show process ID to observe concurrency behavior
    return {
        "name": name,
        "gross": salary,
        "deduction": total_deduction,
        "net": net_salary,
        "pid": os.getpid()
    }   