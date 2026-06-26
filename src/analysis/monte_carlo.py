import random
import numpy as np

def run_simulation(dependencies, iterations=1000):
    null_dist = []
    heads = [d['head'] for d in dependencies]
    
    for _ in range(iterations):
        random.shuffle(heads)
        sampled_dist = [abs(d['id'] - h) for d, h in zip(dependencies, heads)]
        null_dist.append(np.mean(sampled_dist))
        
    return null_dist