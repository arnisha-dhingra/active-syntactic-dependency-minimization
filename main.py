import numpy as np
from src.parser.conllu_parser import load_conllu, extract_dependencies
from src.preprocessing.cleaner import filter_tokens
from src.analysis.dependency_metrics import calculate_mean_distance
from src.analysis.monte_carlo import run_simulation
from src.visualization.plots import plot_null_vs_real

def main():
    # Load and process data
    data = load_conllu('data/sample.conllu')
    dependencies = filter_tokens(extract_dependencies(data[0]))
    
    # Analyze
    real_val = calculate_mean_distance(dependencies)
    null_dist = run_simulation(dependencies)
    
    # Visualize
    plot_null_vs_real(real_val, null_dist, "Universal_Dependencies_Sample")
    print(f"Pipeline executed successfully. Compression Ratio: {np.mean(null_dist)/real_val:.2f}x")

if __name__ == "__main__":
    main()