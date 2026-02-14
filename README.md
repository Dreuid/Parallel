1. Task vs. Data Parallelism
Task Parallelism: Executes different functions concurrently on the same data. Demonstrated in Part A by running four distinct deduction functions on one salary.
Data Parallelism: Executes the same function across multiple data elements. Demonstrated in Part B by applying a single payroll computation to five different employees.

2. concurrent.futures Management
submit(): Schedules a callable and returns a Future object representing the eventual result.
map(): Automatically applies a function to an entire iterable (like the employee list) in parallel.
with Executor: Ensures proper resource management by automatically shutting down worker threads or processes after tasks finish.

3. ThreadPoolExecutor and the GIL
Because of the Global Interpreter Lock (GIL), Python threads cannot execute bytecode simultaneously on multiple cores.
True parallelism did not occur for the computation; instead, the threads take turns, making this better for I/O-bound tasks rather than CPU-heavy math.

4. ProcessPoolExecutor and True Parallelism
This enables true parallelism by creating separate memory spaces for each process, each with its own Python interpreter.
This bypasses the GIL, allowing tasks to run truly simultaneously on different CPU cores.

5. Scalability (5 vs. 10,000 Employees)
Data Parallelism scales better.
While task parallelism is capped by the number of unique functions (only 4 here), data parallelism can distribute thousands of independent records across all available CPU power.

6. Real-World Application
Example: A national bank payroll system.
Data Parallelism: Processing the monthly net pay for 100,000+ accounts using ProcessPoolExecutor.
Task Parallelism: Using ThreadPoolExecutor within a single account to simultaneously fetch tax rates, insurance data, and loan balances from different databases.
