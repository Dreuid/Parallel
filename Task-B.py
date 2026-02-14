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
    
    def run_data_parallelism():
        # Given Employees [cite: 21-26]
    employees = [
        ("Alice", 25000), ("Bob", 32000), ("Charlie", 28000),
        ("Diana", 40000), ("Edward", 35000)
    ]
    
    # Use ProcessPoolExecutor to leverage multiple CPU cores [cite: 80, 88]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Apply the same function to multiple data elements using map() [cite: 58, 83]
        results = list(executor.map(compute_full_payroll, employees))
        
    print(f"\n{'Name':<10} | {'Gross':<10} | {'Total Ded.':<12} | {'Net Salary':<10}")
    print("-" * 50)
    for res in results:
        # Displaying required employee data [cite: 84-87]
        print(f"{res['name']:<10} | {res['gross']:<10.2f} | {res['deduction']:<12.2f} | {res['net']:<10.2f}")

if __name__ == "__main__":
    run_data_parallelism()