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



""" 3. Statistical computing """

"""
    P-value:
        - measure how strength the edivence are with respect to null hypothesis
    
    Permutation test: 
        - A permutation test, also known as an exact test or randomization test
        - is a non-parametric statistical test used to assess the statistical significance of an observed sample statistic.
    
    Monte Carlo Simulation:
        - use for simulating data under the null
    
    
    Bootstrap:
        - Another measure of statistical significance that is better for plotting is the standard error of the mean (SEM)
        

"""


""" 4. Exporation Data Analysis """

"""
     There are two board class of ML approaches commonly used in EDA:
         - 1. Unsupervised learning: aim to find pattern/structure without prior knowledge e.g. clustering 
         - 2. Supervised learning: invovle training a model with labeled example to make prediction e.g. regression
             
             Two main use:
                 1. predict the label on unlablled data
                 2. interpret data: study how predictive model depend on the certain feature of the data.
      
"""





















