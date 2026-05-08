import time
from mpi4py import MPI
from multiprocessing import Lock

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # We keep the Lock to fulfill the synchronization requirement
    lock = Lock()

    if rank == 0:
        print(f"Master Process (rank {rank}) starting task distribution...", flush=True)
        
        orders = [
            {"id": 1, "item": "Keyboard"}, {"id": 2, "item": "Mouse"}, {"id": 3, "item": "Monitor"},
            {"id": 4, "item": "Headset"}, {"id": 5, "item": "Webcam"}, {"id": 6, "item": "Microphone"}
        ]
        
        num_workers = size - 1
        
        # 1. Distribute tasks to workers
        for i, order in enumerate(orders):
            target_worker = (i % num_workers) + 1
            comm.send(order, dest=target_worker, tag=11)
            
        # Send termination signals
        for i in range(1, size):
            comm.send(None, dest=i, tag=11)
            
        # 2. Collect results (Bypassing the Manager() deadlock)
        completed_orders = []
        active_workers = num_workers
        
        while active_workers > 0:
            result = comm.recv(source=MPI.ANY_SOURCE, tag=22)
            if result is None:
                active_workers -= 1
            else:
                completed_orders.append(result)
        
        comm.Barrier()
        
        print("\n--- All tasks completed ---", flush=True)
        print(f"Final Collected Orders List: {completed_orders}", flush=True)
        
    else:
        while True:
            received_order = comm.recv(source=0, tag=11)
            
            if received_order is None:
                # Tell master this worker is shutting down
                comm.send(None, dest=0, tag=22)
                break
                
            print(f"Worker {rank} processing {received_order['item']}", flush=True)
            time.sleep(1)
            
            # 3. Critical Section
            with lock:
                # Send processed order securely back to master
                comm.send(received_order, dest=0, tag=22)
                
        comm.Barrier()

if __name__ == "__main__":
    main()
