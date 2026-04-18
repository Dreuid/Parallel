from multiprocessing import Process, Queue
from search_sequential import sequential_search_competitor

def search_worker(sub_bracket, target_prowess, q, offset):
    for i in range(len(sub_bracket)):
        if sub_bracket[i] == target_prowess:
            q.put(i + offset)
            return
    q.put(-1)

def parallel_search_competitor(bracket, target_prowess):
    block_size = len(bracket) // 4
    if block_size == 0:
        return sequential_search_competitor(bracket, target_prowess)

    blocks = [bracket[i:i + block_size] for i in range(0, len(bracket), block_size)]
    
    q = Queue()
    processes = []
    offset = 0

    for block in blocks:
        p = Process(target=search_worker, args=(block, target_prowess, q, offset))
        processes.append(p)
        p.start()
        offset += len(block)

    competitor_index = -1
    for _ in processes:
        result = q.get()
        if result != -1:
            competitor_index = result

    for p in processes:
        p.join()

    return competitor_index