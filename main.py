import time
# Import from your team's newly created modules
from dataset import generate_tournament_pools
from sorting_sequential import sequential_seed_sort
from sorting_parallel import parallel_seed_sort
from search_sequential import sequential_search_competitor
from search_parallel import parallel_search_competitor

if __name__ == '__main__':
    local_dojo, regional_qualifier, evo_global, seeded_bracket, reverse_seeded_bracket = generate_tournament_pools()
    
    tournament_datasets = {
        "Local Dojo (1k entrants)": local_dojo,
        "Regional Qualifier (100k entrants)": regional_qualifier,
        "EVO Global (1M entrants)": evo_global,
        "Perfectly Seeded (1k)": seeded_bracket,
        "Reverse Seeded (1k)": reverse_seeded_bracket
    }

    print("\n" + "="*50)
    print("--- TOURNAMENT SEEDING (SORTING) EVALUATION ---")
    print("="*50)
    for name, bracket in tournament_datasets.items():
        print(f"\nEvaluating Bracket: {name}")
        
        test_bracket = bracket.copy()
        start = time.time()
        sequential_seed_sort(test_bracket)
        end = time.time()
        print(f"Sequential Seeding Time: {end - start:.6f} seconds")

        test_bracket = bracket.copy()
        start = time.time()
        parallel_seed_sort(test_bracket)
        end = time.time()
        print(f"Parallel Seeding Time:   {end - start:.6f} seconds")

    print("\n" + "="*50)
    print("--- COMPETITOR SEARCH EVALUATION ---")
    print("="*50)
    
    dreuid_prowess_score = 350000

    for name, bracket in tournament_datasets.items():
        print(f"\nSearching Bracket: {name}")
        
        test_bracket = bracket.copy()
        test_bracket.append(dreuid_prowess_score) 
        
        start = time.time()
        seq_idx = sequential_search_competitor(test_bracket, dreuid_prowess_score)
        end = time.time()
        print(f"Sequential Search Time: {end - start:.6f} seconds (Found Dreuid at index {seq_idx})")

        start = time.time()
        par_idx = parallel_search_competitor(test_bracket, dreuid_prowess_score)
        end = time.time()
        print(f"Parallel Search Time:   {end - start:.6f} seconds (Found Dreuid at index {par_idx})")