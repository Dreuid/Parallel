# Distributed Order Processing Challenge

## Team Members
* Lorenz Lacanaria
* Nash Andrew Bondoc
* James Henry Emorricha
* Kyle Martin Sarmiento

## Project Overview
This project simulates a system where a master process generates customer orders and distributes them to multiple worker processes. It demonstrates concurrent execution, process coordination, and safe handling of shared data across isolated memory spaces.

## Environment Setup
* **MPI Implementation:** OpenMPI / MS-MPI (Windows)
* **Python Library:** `mpi4py`
* **Execution Command:** `mpiexec -n 4 python main.py`

## Reflection Questions

**1. How did you distribute orders among worker processes?**
We distributed the orders by having the master process (rank 0) generate the list of tasks, then iterate through them using a modulo operator (`target_worker = (i % num_workers) + 1`). This ensured an even, round-robin distribution. We used `comm.send()` to dispatch the tasks and workers used `comm.recv()` to accept them.

**2. What happens if there are more orders than workers?**
If there are more orders than workers, our round-robin distribution naturally handles the overflow. Because of the modulo logic, workers simply loop back and sequentially take on multiple tasks. For instance, in a 3-worker setup, worker 1 will process order 1, order 4, and order 7 consecutively.

**3. How did processing delays affect the order completion?**
Implementing delays using `time.sleep()` simulated real-world computation bottlenecks. Because the workers processed tasks asynchronously, the final list of completed tasks did not strictly match the chronological sequence in which the master originally distributed them, highlighting how concurrent systems handle variable workloads.

**4. How did you implement shared memory, and where was it initialized?**
We initially implemented shared memory using `multiprocessing.Manager().list()`. However, due to architectural constraints on our Windows environment (where MS-MPI strictly isolates OS-level processes), this caused a system deadlock. To adapt, we pivoted to a safer distributed approach, leveraging MPI's native message passing to securely collect and aggregate the completed task array back in the master process's memory space.

**5. What issues occurred when multiple workers wrote to shared memory simultaneously?**
Before our pivot, we observed two critical issues: severe data inconsistencies (race conditions) when multiple workers appended simultaneously, and an OS-level deadlock caused by isolated MS-MPI processes colliding while trying to establish IPC manager sockets. Shifting to native MPI collection resolved the deadlocks and data loss.

**6. How did you ensure consistent results when using multiple processes?**
To fulfill synchronization requirements and prevent terminal overlapping or race conditions during data transmission, we utilized a `Lock()` from the `multiprocessing` library. We wrapped the worker's transmission phase inside a `with lock:` critical section. This ensured workers waited their turn to securely send their processed orders back to the master.

## Execution Proof
*<img width="400" height="225" alt="Lab1 for final term PDC GROUP" src="https://github.com/user-attachments/assets/444c07a9-407e-400c-8b0d-ee9c8c38f243" />*
