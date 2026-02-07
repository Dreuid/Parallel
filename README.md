1. True Parallelism: Multiprocessing. Each process has its own memory and Python interpreter, allowing them to run on different CPU cores simultaneously.

2. Execution Time Comparison: Multithreading is usually faster for this lab. Creating a "Thread" is lightweight, whereas creating a "Process" is "expensive" and takes more time for the OS to set up.

3. True Parallelism in Threads? No. Python has a Global Interpreter Lock (GIL) which forces threads to take turns. They are "concurrent" (fast switching) but not "parallel" (simultaneous).

4. Scaling to 1000 Grades: Multiprocessing (with a Pool) would eventually win because it uses all CPU cores. Multithreading would slow down because all 1000 threads would still be fighting for the same single-core lock (GIL).

5. CPU-bound vs. I/O-bound: * CPU-bound (Math/Data): Multiprocessing (bypasses GIL).

I/O-bound (Internet/Files): Multithreading (low overhead, good at waiting).

6. Creative Implementation: We used dynamic input handling and high-precision timing with time.perf_counter() to accurately measure the micro-differences between the two methods.
