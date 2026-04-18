from multiprocessing import Process, Queue
from sorting_sequential import sequential_seed_sort, merge_pools

def sort_worker(sub_pool, q):
    sorted_block = sequential_seed_sort(sub_pool)
    q.put(sorted_block)

def parallel_seed_sort(competitors):
    if len(competitors) <= 1:
        return competitors

    block_size = len(competitors) // 4
    if block_size == 0: 
        return sequential_seed_sort(competitors)

    blocks = [competitors[i:i + block_size] for i in range(0, len(competitors), block_size)]
    
    q = Queue()
    processes = []

    for block in blocks:
        p = Process(target=sort_worker, args=(block, q))
        processes.append(p)
        p.start()

    sorted_blocks = []
    for _ in processes:
        sorted_blocks.append(q.get())

    for p in processes:
        p.join()

    while len(sorted_blocks) > 1:
        merged_level = []
        for i in range(0, len(sorted_blocks), 2):
            if i + 1 < len(sorted_blocks):
                merged_level.append(merge_pools(sorted_blocks[i], sorted_blocks[i+1]))
            else:
                merged_level.append(sorted_blocks[i])
        sorted_blocks = merged_level

    return sorted_blocks