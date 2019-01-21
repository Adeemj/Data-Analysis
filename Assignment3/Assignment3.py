# importing numpy library for storing arrays and simple processes on array
import numpy as np
# importing pandas library for reading csv files
import pandas as pd
# importing pyplot from matplotlib to plot graphs
import matplotlib.pyplot as plt
# all libraries as imported as their popular short names

# defining function to find corellation between 2 data
def find_correlation(data_1,data_2):
	correlation = 0.0
	num_terms = len(data_1)

	mean_1 = np.mean(data_1)
	mean_2 = np.mean(data_2)

	for i in range(num_terms):
		correlation += ((data_1[i]-mean_1)*(data_2[i]-mean_2))/(num_terms-1)

	return correlation

# defining number of states and uts, so ecev if number of states gets changed we will need to change only one parameter
num_states = 29
num_uts = 7
num_states_ut = num_states + num_uts

# defining dictionaries for 2 data
names_states_ut = {}
crimerate_dict = {}
unemp_dict = {}

# defining lists for 2 data
crimerate_list = []
unemp_list = []

#defining averages and average standard deviations 
mean_crimerate = 0.0
mean_unemp = 0.0
std_crimerate = 0.0
std_unemp = 0.0

# reading data from csv files
data_crime = pd.read_csv("crimerate.csv")
data_unemp = pd.read_csv("unemploymentrate.csv")

# reading names of states/uts( c(id=2) column) and crimerates ( j(id=9) column)
for i in range(num_states):
	names_states_ut[i] = data_crime.iloc[:,2][i]
	unemp_dict[data_unemp.iloc[:,1][i]] = data_unemp.iloc[:,4][i]
	crimerate_dict[data_crime.iloc[:,2][i]] = data_crime.iloc[:,9][i]
for i in range(num_uts):
	names_states_ut[i+num_states] = data_crime.iloc[:,2][i+num_states+1]
	unemp_dict[data_unemp.iloc[:,1][i+num_states]] = data_unemp.iloc[:,4][i+num_states]
	crimerate_dict[data_crime.iloc[:,2][i+num_states+1]] = data_crime.iloc[:,9][i+num_states+1]

# putting all data in list
for i in range(num_states_ut):
	crimerate_list.append(crimerate_dict[names_states_ut[i]])
	unemp_list.append(unemp_dict[names_states_ut[i]])

# finding mean of data
mean_unemp = np.mean(unemp_list)
mean_crimerate = np.mean(crimerate_list)

# finding standard deviation of data
std_unemp = ((np.var(unemp_list,ddof=1)))**(0.5)
std_crimerate = ((np.var(crimerate_list,ddof=1)))**(0.5)

bins_unemp = np.linspace(0,12,37) # total 36 divisions between 0 to 12
plt.hist(unemp_list,bins=bins_unemp,ec="black") #plotting unemployment data
plt.yticks(np.arange(0,12,1)) # lines parallel to x-axis
# labels for axes
plt.ylabel('Total No. of States and Union Territories')
plt.xlabel('Unemployment Rate (in Percentage)')
# drawing lines for mean and standard deviations
plt.vlines(x = mean_unemp, ymin = 0, ymax = 7)
plt.vlines(x = mean_unemp - std_unemp, ymin = 0, ymax = 7, linestyle="dotted")
plt.vlines(x = mean_unemp + std_unemp, ymin = 0, ymax = 7, linestyle="dotted")
# annotating lines
plt.text(mean_unemp,6,'Mean='+str(round(mean_unemp,3)),ha='center')
plt.annotate(s='',xy=(mean_unemp-std_unemp,4.5),xytext=(mean_unemp,4.5),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.annotate(s='',xy=(mean_unemp+std_unemp,4.5),xytext=(mean_unemp,4.5),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.text(mean_unemp,5,'Standard Deviation='+str(round(std_unemp,3)),ha='center')

plt.grid(axis='y',zorder=0,ls='-.')
# saving figure
plt.savefig('Unemployment.png')

# clearing window
plt.clf()

bins_crimerate = np.linspace(0,1000,41) # total 40 divisions between 0 to 1000
plt.hist(crimerate_list, bins = bins_crimerate, ec = "black") #plotting unemployment data
plt.yticks(np.arange(0,12,1)) # lines parallel to x-axis
# labels for axes
plt.ylabel('Total No. of States and Union Territories')
plt.xlabel('Crime Rate (per 1,00,000)')
# drawing lines for mean and standard deviations
plt.vlines(x = mean_crimerate, ymin = 0, ymax = 9)
plt.vlines(x = mean_crimerate - std_crimerate, ymin = 0, ymax = 9, linestyle="dotted")
plt.vlines(x = mean_crimerate + std_crimerate, ymin = 0, ymax = 9, linestyle="dotted")
# annotating lines
plt.text(mean_crimerate,8,'Mean='+str(round(mean_crimerate,3)),ha='center')
plt.annotate(s='',xy=(mean_crimerate-std_crimerate ,6.5),xytext=(mean_crimerate,6.5),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.annotate(s='',xy=(mean_crimerate+std_crimerate ,6.5),xytext=(mean_crimerate,6.5),arrowprops={'arrowstyle':'<->','shrinkA':0,'shrinkB':0})
plt.text(mean_crimerate,7,'Standard Deviation='+str(round(std_crimerate,3)),ha='center')

plt.grid(axis='y',zorder=0,ls='-.')
# saving figure
plt.savefig('Crimerate.png')

# clearing window
plt.clf()

# plotting scatter plot of crime rate vs unemployment rate
plt.plot(unemp_list,crimerate_list,'ro')
plt.xlabel('Unemployment Rate (in Percentage)')
plt.ylabel('Crime Rate (per 1,00,000)')
# saving figure
plt.savefig('ScatterPlot.png')

# clearing window
plt.clf()

bins = (bins_unemp,bins_crimerate)
plt.hist2d(unemp_list,crimerate_list, bins=bins)
plt.xlabel('Unemployment Rate (in percentage)')
plt.ylabel('Crime Rate (per 100,000)')
# Drawing ColorBar for Information
cbar = plt.colorbar()
cbar.ax.set_ylabel('Counts')

# saving figure
plt.savefig('2D-histogram.png')

# clearing window
plt.clf()

# finding correation using function define in the start of the code
correlation = find_correlation(unemp_list,crimerate_list)

# finding correlation coefficient
correlation_co_eff = (correlation)/((std_unemp*std_crimerate))


# printing some important values to be observed
print("mean_unemp = " + str(mean_unemp))
print("std_unemp = " + str(std_unemp))

print("mean_crimerate = " + str(mean_crimerate))
print("std_crimerate = " + str(std_crimerate))

print("correlation = " + str(correlation))
print("correlation_co_eff = " + str(correlation_co_eff))


