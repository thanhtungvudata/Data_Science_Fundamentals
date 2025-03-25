import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
z = 1.96
x = np.linspace(-4, 4, 1000)
pdf_values = norm.pdf(x)
cdf_values = norm.cdf(x)
p_value = 1 - norm.cdf(z)

# Create a figure with two subplots: PDF and CDF
fig, axs = plt.subplots(2, 1, figsize=(6, 9))

# --- PDF plot (bell curve) ---
axs[0].plot(x, pdf_values, label='Standard Normal PDF', color='blue')
axs[0].axvline(x=z, color='red', linestyle='--', label=f'z = {z}')
axs[0].fill_between(x[x >= z], 0, pdf_values[x >= z], color='red', alpha=0.3, label='p-value area')
axs[0].set_title('PDF of Standard Normal Distribution (One-Tailed)')
axs[0].set_xlabel('Z')
axs[0].set_ylabel('Density')
axs[0].legend()
axs[0].grid(True)

# --- CDF plot (S-curve) ---
axs[1].plot(x, cdf_values, label='Standard Normal CDF', color='blue')
axs[1].axvline(x=z, color='red', linestyle='--', label=f'z = {z}')
axs[1].axhline(y=norm.cdf(z), color='gray', linestyle=':', alpha=0.7)
axs[1].annotate(
    f'p-value ≈ {p_value:.4f}',
    xy=(z + 0.01, norm.cdf(z) + 0.02),
    xytext=(z + 0.3, norm.cdf(z) - 0.1),
    arrowprops=dict(facecolor='red', arrowstyle='->'),
    fontsize=10,
    color='red'
)
axs[1].set_title('CDF of Standard Normal Distribution (One-Tailed)')
axs[1].set_xlabel('Z')
axs[1].set_ylabel('Cumulative Probability')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
