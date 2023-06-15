#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

-> Core Python Scientific Libraries
 
- 1. Numpy: working with array

- 2. Pandas: statistical package: data type( Series and DataFrame)
    https://pandas.pydata.org/docs/user_guide/10min.html#min
    https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
    
- 3. Scipy: higher-level statistical, math and numeric function.    

- 4. Matplotlib: Visualization
    https://matplotlib.org/stable/gallery/index.html 
    https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    
- 5. Scikit-learn: Machine Learning
    https://scikit-learn.org/stable/auto_examples/index.html
    https://www.statlearning.com 

"""

import pandas as pd
import yfinance as yf
import numpy as np
import math
import matplotlib.pyplot as plt

""" 0. Numpy """

points = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]  # example points

# nested loop
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dz = points[i][2] - points[j][2]
        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        distances.append(distance)
print(distances)


# numpy 
points = np.array([(1,2,3), (4,5,6), (7,8,9), (10,11,12)])
# Compute the pairwise differences between points
differences = points[:, np.newaxis] - points

# Compute the squared distances
squared_distances = np.sum(differences**2, axis=2)

# Compute the distances by taking the square root
distances = np.sqrt(squared_distances)

print(distances)


""" 1. Pandas """

# 1. Series
pd.Series([1,3,4])

# set index in series
pd.Series(range(5), index = list('abcde'))

# 2. DataFrame 
pd.DataFrame([[20,20], [21,30], [19,40]] ,
             columns = ["A", "B"], 
             index = list("abc"))


""" 2. Matplotlib """

"""
    - barplot
    - historgram
    - scatterplot
    - line and area plot
    * Always label axes, lines, etc. (Best Practice)
"""

stock_data = yf.download("SISB.BK", start = "2021-06-07", end = "2023-06-07") 

# Line Plot
stock_data['Close'].plot()
plt.title("Stock Close Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

# Bar Plot
stock_data['Volume'].plot(kind = 'bar')
plt.title("Stock Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

# Histogram
stock_data['Close'].plot(kind='hist')
plt.title("Stock Close Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
stock_data.plot.scatter(x='Open', y='Close')
plt.title("Stock Open vs Close")
plt.xlabel("Open Price")
plt.ylabel("Close Price")
plt.show()


# Calculate one month lag
one_month_lag = stock_data['Close'].shift(256)
# Scatter Plot
plt.scatter(one_month_lag, stock_data['Close'])
plt.title("Price from One Month Lag vs. Present Price")
plt.xlabel("Price from One Month Lag")
plt.ylabel("Present Price")
plt.show()






# Area Plot
stock_data[['Open', 'Close']].plot.area()
plt.title("Stock Open vs Close")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()


""" 3. Statistical computing """

"""
        P-value:
            - measure how strength the edivence are with respect to null hypothesis
            - measure statistical significant
            - sampling without replacement
    
    1. Permutation test: 
        - A permutation test, also known as an exact test or randomization test
        - is a non-parametric statistical test used to assess the statistical significance of an observed sample statistic.
        - Pr{Value this or more extreme | null hypothesis is true }
        - Pr{do good as original | random data } 
        
        
        - p-value:
            > 0.05 : nothing there - Certainly
            < 0.05 : maybe something here (might need bigger experiment) Week evidence
            < 0.001 : Strong evidence
        
        Process
            1. Simulate truth value:
            - randomize it so that truth have random change
            - use montec carlo to get null hypothesis 1000x
            
        
            
            2. Compute P-value: count / 1000  
            - Use computer to predict the truth value given it has no prior knowledge.
            - count how many iteration the effect size is as larage as it was in the original experitment.
            
        
            Monte Carlo Simulation:
                - use for simulating data under the null
            
    2. Bootstrap:
        - Another measure of statistical significance that is better for plotting is the standard error of the mean (SEM)
        - simulate repeated sampling a sample with replacement in sample itself


"""
# Permutation test: calculate p-value 

# emperical experiment: Chim win the game 3/4, how much evidence show that it happen by luck?
original_data = pd.DataFrame({'W': [1, 1, 1, 0], 'L': [0, 0, 0, 1]}, index=['Round_1', 'Round_2', 'Round_3', 'Round_4'])

# null case
truth = [1] * 4 + ['0'] * 4

tail_num = 0 # tail area probability (rare situation)
n_permutations = 1000

# Compute accuracy for the original case (75%)
acc_truth = (original_data.loc['Round_1','W'] 
             + original_data.loc['Round_2','W'] 
             + original_data.loc['Round_3','W']
             + original_data.loc['Round_4','W'])   / original_data.sum().sum()

for _ in range(n_permutations):
    guess = np.random.permutation(truth) # random generator
    
    acc_tt = np.count_nonzero(guess[:4] == '1') / len(original_data)
    
    if acc_tt >= acc_truth:
        tail_num += 1

p_val = tail_num / n_permutations # prob{of the time that computer do at least as good as me}
print(f"p value: {p_val} chance that Chim win the game because his luck")


""" 4. Exporation Data Analysis """

"""
     There are two board class of ML approaches commonly used in EDA:
         - 1. Unsupervised learning: aim to find pattern/structure without prior knowledge e.g. clustering 
         - 2. Supervised learning: invovle training a model with labeled example to make prediction e.g. regression
         
         
             e.g. 
             1. k-nearest neighbour 
             2. pending Lec. May 9
             
             Two main use:
                 1. predict the label on unlablled data (reg)
                 2. interpret data: study how predictive model depend on the certain feature of the data. (classify)
"""



# k mean 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = iris.data[:, :2]  # Consider only the first two features for simplicity
y = iris.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=100)

# Train the classifier
knn.fit(X_train, y_train)

# Define the range of feature values for the plot
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

# Generate a grid of points within the feature value range
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

# Make predictions on the grid points
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

# Reshape the predicted labels to match the grid shape
Z = Z.reshape(xx.shape)

# Create a scatter plot of the data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')

# Plot the decision boundaries
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Set1)

# Set the axis labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('KNN Decision Boundaries')

# Show the plot
plt.show()












