def merge_pools(left_pool, right_pool):
    seeded = []
    i = j = 0
    while i < len(left_pool) and j < len(right_pool):
        if left_pool[i] < right_pool[j]:
            seeded.append(left_pool[i])
            i += 1
        else:
            seeded.append(right_pool[j])
            j += 1
    seeded.extend(left_pool[i:])
    seeded.extend(right_pool[j:])
    return seeded

def sequential_seed_sort(competitors):
    if len(competitors) <= 1:
        return competitors
    mid = len(competitors) // 2
    left_pool = sequential_seed_sort(competitors[:mid])
    right_pool = sequential_seed_sort(competitors[mid:])
    return merge_pools(left_pool, right_pool)