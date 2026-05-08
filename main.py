from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        print(f"Master Process (rank {rank}) starting task distribution...", flush=True)

        orders = [
            {"id": 1, "item": "Keyboard"}, {"id": 2, "item": "Mouse"}, {"id": 3, "item": "Monitor"},
            {"id": 4, "item": "Headset"}, {"id": 5, "item": "Webcam"}, {"id": 6, "item": "Microphone"}
        ]

        num_workers = size - 1

        for i, order in enumerate(orders):
            target_worker = (i % num_workers) + 1
            comm.send(order, dest=target_worker, tag=11)

        for i in range(1, size):
            comm.send(None, dest=i, tag=11)

    else:
        while True:
            received_order = comm.recv(source=0, tag=11)
            if received_order is None:
                break

            print(f"Worker {rank} processing {received_order['item']}", flush=True)

if name == "main":
    main()

import time
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        print(f"Master Process (rank {rank}) starting task distribution...", flush=True)

        orders = [
            {"id": 1, "item": "Keyboard"}, {"id": 2, "item": "Mouse"}, {"id": 3, "item": "Monitor"},
            {"id": 4, "item": "Headset"}, {"id": 5, "item": "Webcam"}, {"id": 6, "item": "Microphone"}
        ]

        num_workers = size - 1

        for i, order in enumerate(orders):
            target_worker = (i % num_workers) + 1
            comm.send(order, dest=target_worker, tag=11)

        for i in range(1, size):
            comm.send(None, dest=i, tag=11)

Collect results,
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
                comm.send(None, dest=0, tag=22)
                break

            print(f"Worker {rank} processing {received_order['item']}", flush=True)
            time.sleep(1)

Send processed order back to master,
            comm.send(received_order, dest=0, tag=22)

        comm.Barrier()

if name == "main":
    main()
