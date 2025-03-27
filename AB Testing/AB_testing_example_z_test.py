import numpy as np
import scipy.stats as stats

# Simulated data
# Group A (Control): 1000 users, 120 conversions
# Group B (Variant): 1000 users, 138 conversions

control_conversions = 120
variant_conversions = 138
control_total = 1000
variant_total = 1000

# Conversion rates
p1 = control_conversions / control_total
p2 = variant_conversions / variant_total
p_pooled = (control_conversions + variant_conversions) / (control_total + variant_total)

# Standard error
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/control_total + 1/variant_total))

# z-score
z = (p2 - p1) / se

# p-value
p_val = 1 - stats.norm.cdf(z)

print(f"Control conversion rate: {p1:.2%}")
print(f"Variant conversion rate: {p2:.2%}")
print(f"Z-score: {z:.4f}")
print(f"P-value: {p_val:.4f}")