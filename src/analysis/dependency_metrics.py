import numpy as np

def calculate_mean_distance(dependencies):
    distances = [d['distance'] for d in dependencies]
    return np.mean(distances) if distances else 0

def calculate_scaling(dependency_groups):
    # Analyzing scaling behavior (e.g., avg distance vs sentence length)
    scaling_stats = {}
    for length, data in dependency_groups.items():
        scaling_stats[length] = calculate_mean_distance(data)
    return scaling_stats