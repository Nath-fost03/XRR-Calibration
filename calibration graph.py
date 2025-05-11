# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:53:07 2024

@author: natha
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

#raw data
power_values = [15, 20, 25, 30, 35]  
growth = [102.01, 140.27, 163.38, 181.75, 207.01]  

# convert values into an array
growth = np.array(growth) 
# Convert total growth to growth rate per second
growth_rate_values = (growth / 120)   


slope, intercept, r_value, p_value, std_err = linregress(power_values, growth_rate_values)


slope_uncertainty = std_err  
intercept_uncertainty = std_err * np.sqrt(np.mean(np.square(power_values)))  

# Calculate y-values
line_y_values = slope * np.array(power_values) + intercept

# Print results with uncertainties
print(f"Slope (gradient): {slope:.4f} ± {slope_uncertainty:.4f}")
print(f"Intercept (y-intercept): {intercept:.4f} ± {intercept_uncertainty:.4f}")

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(power_values, line_y_values, color='r', linestyle='--', label=f'Best fit: y={slope:.2f}x + {intercept:.2f}')
plt.scatter(power_values, growth_rate_values, label="Data", color='b')

plt.xlabel('Power (W)')
plt.ylabel('Growth Rate (10^(-10)m) ')
plt.legend()
plt.grid(True)


plt.show()
