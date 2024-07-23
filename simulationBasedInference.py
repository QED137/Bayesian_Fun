import numpy as np
import matplotlib.pyplot as plt

# Define the prior distribution p(θ) - we use a normal distribution for this example
def prior_distribution():
    return np.random.normal(loc=0, scale=1)  # mean = 0, std = 1

# Define the likelihood function p(x_o | θ) - we use a simple example here
def likelihood_function(theta, x_o):
    # For example, we use a normal distribution with mean θ and fixed std
    return np.exp(-0.5 * ((x_o - theta) ** 2))

# Rejection sampling algorithm
def rejection_sampling(N, x_o):
    samples = []
    for _ in range(N):
        theta = prior_distribution()
        acceptance_prob = likelihood_function(theta, x_o)
        if np.random.uniform(0, 1) < acceptance_prob:
            samples.append(theta)
    return samples

# Parameters
N = 10000  # Number of samples
x_o = 0.5  # Observed data

# Run the rejection sampling algorithm
samples = rejection_sampling(N, x_o)

# Plot the histogram of the accepted samples
plt.hist(samples, bins=50, density=True, alpha=0.6, color='g')
plt.title('Histogram of Accepted Samples')
plt.xlabel('θ')
plt.ylabel('Density')
plt.show()
plt.savefig()

