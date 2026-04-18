def sequential_search_competitor(bracket, target_prowess):
    for i in range(len(bracket)):
        if bracket[i] == target_prowess:
            return i
    return -1