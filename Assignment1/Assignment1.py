#Importing libraries numpy for data handling and matplotlib for plotting histogram
import numpy as np 
import matplotlib.pyplot as plt

#Reading data from appropriate columns of csv file, Typecasting data from String to Float and Storing it in list 
array = []
for i,line in enumerate( open('pre_primary_school_data.csv')):
    if i > 0:    
        full_row = line.split(',')
        req_row = []
        for j in range(3):
            req_row.append(float( full_row[12 + j] ))
        array.append(req_row)

#List converted to numpy main_matrix
main_matrix = np.array(array)

#Getting the size of the numpy main_matrix
(a, b) = main_matrix.shape

#Declaring and initializing array to store total number of teachers
total_teachers_array = np.zeros(a)
for i in range(a):
    total_teachers_array[i] = (main_matrix[i][1]+main_matrix[i][2])

#Converting the array to a matrix for concatanation to main_matrix
total_teachers_matrix = total_teachers_array.reshape(a, 1)
main_matrix = np.concatenate( (main_matrix,total_teachers_matrix), axis=1)

#Declaring and initializing an array to store number of teachers per school
teachers_per_school_array = np.zeros(a)
for i in range(a):
    if main_matrix[i][0] != 0:
        teachers_per_school_array[i] = main_matrix[i][3] / main_matrix[i][0]

#Converting the array to a matrix for concatanation to main_matrix
teachers_per_school_matrix = teachers_per_school_array.reshape(a, 1)
main_matrix = np.concatenate( (main_matrix,teachers_per_school_matrix), axis=1)

#Declaring and initializing a dictionary for teachers per school
teachers_per_school={}
teachers_per_school[ "rural" ] = np.zeros( int(a / 3) - 1)
teachers_per_school[ "urban" ] = np.zeros( int(a / 3) - 1 )
teachers_per_school[ "total" ] = np.zeros( int(a / 3) - 1)
for i in range(a - 3):
    current=teachers_per_school_array[i]
    if i % 3 == 0:
        teachers_per_school[ 'rural' ][ int(i / 3) ] = current
    elif i % 3 == 1:
        teachers_per_school[ 'urban' ][int(i / 3) ] = current
    else:
        teachers_per_school[ 'total' ][ int(i / 3) ] = current

#Plotting and showing required histograms with optimum bins
plt.hist( teachers_per_school[ 'rural' ], bins = 7, color = 'b')
plt.xlabel('Teachers per school rural')
plt.ylabel('No of states')
plt.title('Pre primary teachers per school distribution - rural')
plt.show()

plt.hist( teachers_per_school[ 'urban' ], bins = 5, color = 'b')
plt.xlabel('Teachers per school urban')
plt.ylabel('No of states')
plt.title('Pre primary teachers per school distribution - urban')
plt.show()

plt.hist( teachers_per_school[ 'total' ], bins = 7, color='b')
plt.xlabel('Teachers per school total')
plt.ylabel('No of states')
plt.title('Pre primary teachers per school distribution - total')
plt.show()
