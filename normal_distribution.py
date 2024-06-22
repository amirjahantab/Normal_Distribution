import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Define the standard normal distribution
mu = 0
sigma = 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)

# Z-score
z_score = 1.25

# Plot the standard normal distribution curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Distribution')

# Shade the area for Z < 1.25
x_fill = np.linspace(mu - 4*sigma, z_score, 1000)
y_fill = stats.norm.pdf(x_fill, mu, sigma)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label=f'P(Z < {z_score})')

# Add lines and labels
plt.axvline(x=z_score, color='red', linestyle='--', label=f'Z = {z_score}')
plt.axhline(y=0, color='black', linestyle='-')
plt.title('Standard Normal Distribution and Z-Score')
plt.xlabel('Z')
plt.ylabel('Probability Density')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
