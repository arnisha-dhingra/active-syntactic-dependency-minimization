import matplotlib.pyplot as plt
import seaborn as sns

def plot_null_vs_real(real_val, null_dist, lang_name):
    plt.figure(figsize=(10, 6))
    sns.kdeplot(null_dist, fill=True, label='Randomized (Null)')
    plt.axvline(real_val, color='r', linestyle='--', label=f'Real Observed: {real_val:.2f}')
    plt.title(f'Efficiency Analysis: {lang_name}')
    plt.legend()
    plt.savefig(f'analysis_results_{lang_name}.png')
    plt.close()