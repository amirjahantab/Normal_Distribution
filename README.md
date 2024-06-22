## README.md

# Understanding the Normal Distribution and the Standard Normal Table

## Table of Contents

1. [Introduction](#introduction)
2. [Normal Distribution](#normal-distribution)
    - [Definition](#definition)
    - [Characteristics](#characteristics)
    - [Formula](#formula)
3. [Standard Normal Distribution](#standard-normal-distribution)
    - [Definition](#definition-1)
    - [Z-Score](#z-score)
    - [Formula](#formula-1)
4. [Standard Normal Table](#standard-normal-table)
    - [Definition](#definition-2)
    - [How to Use the Z-Table](#how-to-use-the-z-table)
5. [Example Usage](#example-usage)
6. [Visual Representation](#visual-representation)
    - [Diagram Explanation](#diagram-explanation)
    - [Code Explanation](#code-explanation)
7. [Conclusion](#conclusion)

## Introduction

This document provides a comprehensive guide to understanding the normal distribution, the standard normal distribution, and the standard normal table (Z-table). These concepts are fundamental in statistics and are widely used for various statistical analyses, including hypothesis testing and confidence interval estimation.

## Normal Distribution

### Definition

The normal distribution, also known as the Gaussian distribution, is a continuous probability distribution that is symmetric around its mean. It describes how the values of a variable are distributed. In many real-world situations, data tends to be distributed in a pattern that approximates the normal distribution.

### Characteristics

- **Bell-Shaped Curve**: The graph of a normal distribution is bell-shaped and symmetric about the mean.
- **Mean, Median, and Mode**: In a normal distribution, these three measures of central tendency are equal and located at the center of the distribution.
- **Empirical Rule**: Approximately 68% of the data falls within one standard deviation of the mean, 95% within two standard deviations, and 99.7% within three standard deviations.

### Formula

The probability density function (PDF) of a normal distribution is given by:

\[ f(x | \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{ -\frac{1}{2} \left( \frac{x - \mu}{\sigma} \right)^2 } \]

where:
- \( \mu \) is the mean,
- \( \sigma \) is the standard deviation,
- \( x \) is the value of the random variable.

## Standard Normal Distribution

### Definition

The standard normal distribution is a special case of the normal distribution with a mean (\(\mu\)) of 0 and a standard deviation (\(\sigma\)) of 1. It is used as a reference to understand and compare different normal distributions.

### Z-Score

The Z-score is a measure that describes a value's position relative to the mean of a group of values, measured in terms of standard deviations from the mean. It is calculated using the formula:

\[ Z = \frac{X - \mu}{\sigma} \]

where:
- \( X \) is the value,
- \( \mu \) is the mean,
- \( \sigma \) is the standard deviation.

### Formula

The probability density function (PDF) for the standard normal distribution simplifies to:

\[ f(z) = \frac{1}{\sqrt{2\pi}} e^{ -\frac{z^2}{2} } \]

## Standard Normal Table

### Definition

A standard normal table, also known as a Z-table, provides the cumulative probability of a standard normal distribution up to a given Z-score. It helps in determining the probability that a standard normal random variable is less than or equal to a given value.

### How to Use the Z-Table

1. **Find the Z-Score**: Calculate the Z-score for your data point.
2. **Locate the Z-Score in the Table**: The Z-table is typically structured with Z-scores in the margins. The rows represent the first two digits, and the columns represent the hundredths place.
3. **Read the Cumulative Probability**: The intersection of the row and column gives the cumulative probability up to that Z-score.

## Example Usage

Suppose you have a Z-score of 1.25:

1. **Locate the row** for 1.2.
2. **Locate the column** for 0.05.
3. **Find the intersection**: The table value at this intersection represents the cumulative probability up to Z = 1.25.

For instance, the table might show 0.8944, meaning that approximately 89.44% of the values lie below a Z-score of 1.25.

## Visual Representation

Here’s a visual representation to help you understand the standard normal distribution and how the Z-table is used.

### Diagram Explanation

1. **Standard Normal Distribution Curve**: The curve is symmetric around the mean (0). The area under the curve represents the total probability, which is 1.
2. **Z-Score and Cumulative Probability**: The Z-score is plotted on the horizontal axis. The area under the curve to the left of a given Z-score represents the cumulative probability.
3. **Example with Z = 1.25**: 
   - Locate Z = 1.25 on the horizontal axis.
   - Shade the area under the curve to the left of Z = 1.25. 
   - This shaded area corresponds to the cumulative probability from the Z-table.

### Code Explanation

Let's break down the code used to generate the diagram step by step.

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
```

- `matplotlib.pyplot` is a library used for plotting graphs.
- `numpy` is a library for numerical operations.
- `scipy.stats` provides functions for statistical operations.

```python
# Define the standard normal distribution
mu = 0
sigma = 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = stats.norm.pdf(x, mu, sigma)
```

- `mu` is the mean of the distribution (0 for standard normal).
- `sigma` is the standard deviation (1 for standard normal).
- `x` is an array of values from -4 to 4 (covering almost all the area under the curve).
- `y` is the probability density function (PDF) values for each `x`.

```python
# Z-score
z_score = 1.25
```

- `z_score` is the Z-score we are interested in.

```python
# Plot the standard normal distribution curve
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Standard Normal Distribution')
```

- `plt.figure(figsize=(10, 6))` creates a plot with specified dimensions.
- `plt.plot(x, y, label='Standard Normal Distribution')` plots the standard normal distribution curve.

```python
# Shade the area for Z < 1.25
x_fill = np.linspace(mu - 4*sigma, z_score, 1000)
y_fill = stats.norm.pdf(x_fill, mu, sigma)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label=f'P(Z < {z_score})')
```

- `x_fill` is an array of values from -4 to 1.25.
- `y_fill` is the PDF values for `x_fill`.
- `plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.4, label=f'P(Z < {z_score})')` shades the area under the curve from -4 to 1.25.

```python
# Add lines and labels
plt.axvline(x=z_score, color='red', linestyle='--', label=f'Z = {z_score}')
plt.axhline(y=0, color='black', linestyle='-')
plt.title('Standard Normal Distribution and Z-Score')
plt.xlabel('Z')
plt.ylabel('Probability Density')
plt.legend()
```

- `plt.axvline(x=z_score, color='red', linestyle='--', label=f'Z = {z_score}')` draws a vertical line at Z = 1.25.
- `plt.axhline(y=0, color='black', linestyle='-')` draws the horizontal axis.
- `plt.title('Standard Normal Distribution and Z-Score')` adds a title to the plot.
- `plt.xlabel('Z')` labels the x-axis.
- `plt.ylabel('Probability Density')` labels the y-axis.
- `plt.legend()` displays the legend for the plot.

```python
# Display the plot
plt.grid(True)
plt.show()
```

- `plt.grid(True)` adds a grid to the plot.
- `plt.show()` displays the plot.

## Conclusion

Understanding the normal distribution and the standard normal table is crucial for statistical analysis. The normal distribution describes how data is spread around the mean, while the standard normal table helps find probabilities and make inferences about the data. By mastering these concepts, you can effectively analyze and interpret data in various fields, from finance to social sciences.
