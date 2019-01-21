# importing numpy library for sorting arrays and simple processes on array
import numpy as np
# importing pandas library for reading csv files
import pandas as pd
# importing pyplot from matplotlib to plot graphs
import matplotlib.pyplot as plt
# importing math library to perform math functions
import math

# defining function to find the integration (number of events) of single bin of background histogram
def integrate_background(low_limit, up_limit):
	return (10000*(math.exp(-(low_limit/10.0)) - math.exp(-(up_limit/10.0))))

# defining function to find the integration (number of events) of single bin of darkmatter data/histogram
def integrate_darkmatter(low_limit, up_limit, sigma):
	if (low_limit >= 5 and up_limit <= 15):
		return (sigma*20*(((up_limit**2) - (low_limit**2))/2.0 - 5.0))
	elif (low_limit >= 15 and up_limit <= 25):
		return (sigma*20*(25.0 - ((up_limit**2) - (low_limit**2))/2.0)) 	
	else:
		return 0.0

# defining lists to store log_likelihood values and parameter values
log_likelihood = []
s_axis = []

# defining function to find log_likelihood of histograms (background + darkmatter data)
def generate_likelihood():
	flag = 0
	i = 36.0 
	while i <= 39:
		log_likelihood.append(0)
		s = 10**(i - 39)
		s_axis.append(i)
		for j in range(0, 40):
			mean = integrate_darkmatter(j, j+1, s) + integrate_background(j, j+1)
			log_likelihood[flag] += (-1)*(mean) + data[' Number of events'][j]*math.log(mean)
		i += 0.04
		flag += 1

# defining function to find the derivative of likelihood function
def derivative(array):
	array_prime = []
	for i in range(0, (len(array) - 1)):
		value = (array[i+1] - array[i])/(s_axis[i+1] - s_axis[i]) 
		array_prime.append(value)
	return array_prime

# reading data from csv files
data = pd.read_csv('recoilenergydata_EP219.csv')

# plotting histogram of the given data
plt.bar(data['E_R (KeV)'], data[' Number of events'], width = 1, align = 'center')
plt.title('Histogram of the given Data')
plt.xlabel('E_R (KeV)')
plt.ylabel('Number of events')
plt.show()

# defining list to store mean value for each bin of background data
background_mean = []
for i in range(0, 40):
	background_mean.append(integrate_background(i, i+1))

plt.bar(data['E_R (KeV)'], background_mean, width = 1, align = 'center')	
plt.title('Histogram of background')
plt.xlabel('E_R (KeV)')
plt.ylabel('Number of events')
plt.show()

# defining list to store different values of sigma
number_of_events_mean_s = [1, 2, 3, 4, 5]

# plotting the histogram for background + signal
s = 0.01*(10**(-39))
for i in range(0, 5):
	number_of_events_mean_s[i] = []
	for j in range(0, 40):
		number_of_events_mean_s[i].append(integrate_darkmatter(j, j+1, s))

	for k in range(0, 40):
		number_of_events_mean_s[i][k] = background_mean[k] + number_of_events_mean_s[i][k]
	plt.bar(data['E_R (KeV)'], number_of_events_mean_s[i], width = 1, align = 'center')
	plt.title('Histogram of the signal for sigma = ' + str(s))
	plt.xlabel('E_R (KeV)')
	plt.ylabel('Number of events')
	plt.show()
	s = s*10

# calling the generate_likelihood function			
generate_likelihood()

# plotting log_likelihood function with respect to the parameter sigma			
plt.plot(s_axis, log_likelihood)
plt.title('plot of log likelihood')
plt.xlabel('log10(parameter), where parameter is in fb')
plt.ylabel('log likelihood')
plt.show()

# finding the first derivative of the log_likelihood function
log_like_prime = derivative(log_likelihood)

# finding the second derivative of the log_likelihood function
log_like_double_prime = derivative(log_like_prime)

# finding the error delta (spread in log_likelihood plot)
delta = -1/(log_like_double_prime[np.argmax(log_likelihood)])

# printing the value of sigma at which log_likelihood is maximum
print('value of sigma at which log likelihood is maximum is: ', 10**(s_axis[np.argmax(log_likelihood)] - 39))

# printing the error/spread in log_likelihood plot
print('error/spread in likelihood function is:', math.sqrt(delta))

