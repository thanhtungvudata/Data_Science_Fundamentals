from scipy.stats import ttest_ind

# Simulated time-on-page data (in seconds)
group_A = [120, 130, 115, 123, 140]
group_B = [150, 160, 145, 155, 170]

# Welch's t-test (does not assume equal variances)
t_stat, p_value = ttest_ind(group_B, group_A, equal_var=False)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
