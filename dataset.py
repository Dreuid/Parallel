import random

def generate_tournament_pools():
    print("Generating King of Iron Fist entrant pools (Tekken Prowess Scores)...")
    
    local_dojo = [random.randint(10000, 400000) for _ in range(1000)]
    regional_qualifier = [random.randint(10000, 400000) for _ in range(100000)]
    evo_global = [random.randint(10000, 400000) for _ in range(1000000)]
    
    seeded_bracket = sorted(local_dojo.copy())
    reverse_seeded_bracket = sorted(local_dojo.copy(), reverse=True)
    
    return local_dojo, regional_qualifier, evo_global, seeded_bracket, reverse_seeded_bracket