import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
z = 1.96
x = np.linspace(-4, 4, 1000)
pdf_values = norm.pdf(x)
cdf_values = norm.cdf(x)
p_one_tail = 1 - norm.cdf(z)
p_two_tail = 2 * p_one_tail

# Create a figure with two subplots: PDF and CDF
fig, axs = plt.subplots(2, 1, figsize=(6, 9))

# --- PDF plot (bell curve) ---
axs[0].plot(x, pdf_values, label='Standard Normal PDF', color='blue')

# Vertical lines
axs[0].axvline(x=z, color='red', linestyle='--', label=f'z = ±{z}')
axs[0].axvline(x=-z, color='red', linestyle='--')

# Shaded tails (both sides)
axs[0].fill_between(x[x >= z], 0, pdf_values[x >= z], color='red', alpha=0.3)
axs[0].fill_between(x[x <= -z], 0, pdf_values[x <= -z], color='red', alpha=0.3, label='p-value area (2-tailed)')

# Labels
axs[0].set_title('PDF of Standard Normal Distribution (Two-Tailed)')
axs[0].set_xlabel('Z')
axs[0].set_ylabel('Density')
axs[0].legend()
axs[0].grid(True)

# --- CDF plot (S-curve) ---
axs[1].plot(x, cdf_values, label='Standard Normal CDF', color='blue')
axs[1].axvline(x=z, color='red', linestyle='--', label=f'z = ±{z}')
axs[1].axvline(x=-z, color='red', linestyle='--')

# Horizontal lines and annotations for both tails
axs[1].axhline(y=norm.cdf(z), color='gray', linestyle=':', alpha=0.7)
axs[1].axhline(y=norm.cdf(-z), color='gray', linestyle=':', alpha=0.7)

# Annotate p-value
axs[1].annotate(
    f'p-value/2 ≈ {p_two_tail/2:.4f}',
    xy=(z + 0.01, norm.cdf(z) + 0.02),
    xytext=(z + 0.3, norm.cdf(z) - 0.1),
    arrowprops=dict(facecolor='red', arrowstyle='->'),
    fontsize=10,
    color='red'
)
axs[1].annotate(
    f'p-value/2 ≈ {p_two_tail/2:.4f}',
    xy=(-z - 0.01, norm.cdf(-z) - 0.02),
    xytext=(-z - 2, norm.cdf(-z) + 0.1),
    arrowprops=dict(facecolor='red', arrowstyle='->'),
    fontsize=10,
    color='red'
)

# Labels
axs[1].set_title('CDF of Standard Normal Distribution (Two-Tailed)')
axs[1].set_xlabel('Z')
axs[1].set_ylabel('Cumulative Probability')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
