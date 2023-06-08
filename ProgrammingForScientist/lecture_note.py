#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

-> Summary lecture note: Programming for Scientist.

"""


""" 1. List """

# most method modify itself: extend, append, insert, sort, pop(1), remove("A"), reverse
myList = list([2,3,4,6])
myList = list()
myList = [2,3,4,6]

# List comprehension
[number*2 for number in myList if number % 2 == 0 ] 

# make copy
b = myList[:]

""" 2. Tuple : unmutable """

myTuple = ("A","B")

""" 3. Dict (HashMap) : no order """

myDict = {"A": 1, "B": 2, "C" : 3}

myDict.keys()
myDict.values()
myDict.items()

# remove
myDict.pop("A")

# remove last item
myDict.popitem()



""" 4. String """

# strip, replace 
myString = "Nanthawat Anan?   "
myString.strip("?")
myString.replace("Anan", "Chim")
myString.strip()

# .format 
symbol = "AOT"
country = "BK"
name = "{}.{}".format(symbol, country)


# function 
import pandas as pd
def convert_string_to_df(string_data):
    """
    Convert a string into a DataFrame by splitting it using the "|" delimiter.

    Parameters
    ----------
    string_data : str
        The string data to be converted into a DataFrame. It should contain rows separated by newline characters
        and columns separated by the "|" delimiter.

    Returns
    -------
    pandas.core.frame.DataFrame
        The resulting DataFrame with columns split based on the delimiter.

    """
    rows = string_data.split("\n")
    columns = [row.split("|") for row in rows]
    df = pd.DataFrame(columns)
    return df
    

string_data = """ 2020-05-19|2857|1DIV|N|10.50490|L|0|0|0||7.90|2020-05-18|7.99|8.09|7.99|8.09|8.09|8.10|0.19|100|29900|239737.00|16|0|0.00|0|8.02|0|0.00|0.00||N|N|||N||11.56|N.A.|12|2019-06-30|0.24|| ||||0.70|6.18|95193671||770116798.39|THB|THSEHD070009||
2020-05-19|2858|1DIV|Y|10.50490|L|0|0|0||7.82|2020-05-15|0.00|0.00|0.00|0.00|0.00|0.00|0.00|100|0|0.00|0|0|0.00|0|0.00|0|0.00|0.00||N|N|||N||||||||||||||95193671|||THB|||
2020-05-19|1966|7UP|Y|1.00000|S|6|9|0|Energy & Utilities|0.44|2020-05-18|0.43|0.43|0.42|0.43|0.42|0.44|-0.01|100|52|22.19|8|0|0.00|0|0.43|0|0.00|0.00||N|N|||N||||||||||||||3029598102|||THB|||
2020-05-19|1965|7UP|N|1.00000|S|6|9|0|Energy & Utilities|0.42|2020-05-18|0.42|0.44|0.41|0.44|0.43|0.44|0.02|100|21421900|9141665.00|239|0|0.00|0|0.43|0|0.00|0.00||N|N|||N||0.48|0.013|3|2020-03-31|0.00|12||2019-12-31|9.10| |0.91|0.00|3029598102||1333023164.88|THB|TH0670A10Y03|TH0670010R18|
2020-05-19|1967|7UP-F|N|1.00000|F|6|9|0|Energy & Utilities|6.00|2007-12-27|0.00|0.00|0.00|0.00|0.00|0.00|0.00|100|0|0.00|0|0|0.00|0|0.00|0|0.00|0.00||N|N|||N||||||||||||||3029598102|||THB|TH0670A10Y11||
2020-05-19|45136|7UP-W4|N|0.00000|W|0|0|0||0.12|2020-05-18|0.12|0.13|0.12|0.12|0.12|0.13|0.00|100|6792100|871663.00|106|0|0.00|0|0.13|0|0.00|0.00||N|N|||N||||||||||||||605919620||72710354.40|THB|TH0670052800|TH06700528R6|
2020-05-19|45137|7UP-W4|Y|0.00000|W|0|0|0||0.06|2020-05-14|0.00|0.00|0.00|0.00|0.06|0.00|0.00|100|0|0.00|0|0|0.00|0|0.00|0|0.00|0.00||N|N|||N||||||||||||||605919620|||THB|||
2020-05-19|1775|A|N|1.00000|S|5|25|0|Property Development|4.70|2020-05-18|4.68|4.70|4.60|4.66|4.58|4.66|-0.04|100|20600|95544.00|14|0|0.00|0|4.64|0|0.00|0.00||N|N|||N||3.47|0.001|3|2020-03-31|0.00|12||2019-12-31|N.A.| |1.34|0.00|980000000||4566800000.00|THB|TH0770010Z08|TH0770010R16|
2020-05-19|1776|A|Y|1.00000|S|5|25|0|Property Development|4.66|2020-05-08|4.68|4.68|4.68|4.68|4.66|5.40|0.02|100|1|4.68|1|0|0.00|0|4.68|0|0.00|0.00||N|N|||N||||||||||||||980000000|||THB|||
2020-05-19|4263|AAV|Y|0.10000|S|7|28|0|Transportation & Logistics|1.68|2020-05-18|1.73|1.85|1.73|1.80|1.79|1.85|0.12|100|1017|1813.46|47|0|0.00|0|1.78|0|0.00|0.00||N|N|||N||||||||||||||4850000000|||THB|||
2020-05-19|4262|AAV|N|0.10000|S|7|28|0|Transportation & Logistics|1.67|2020-05-18|1.75|1.83|1.73|1.80|1.79|1.80|0.13|100|114443100|204467923.00|4893|0|0.00|0|1.79|170000|302900.00|1.781764||N|N|||N||3.53|-0.13845|3|2020-03-31|0.00|12||2018-12-31|N.A.| |0.51|0.00|4850000000||8730000000.00|THB|TH3437010004|TH3437010R19|
2020-05-19|50732|AAV13C2007A|N|0.00000|V|0|0|0||0.04|2020-05-18|0.04|0.06|0.03|0.06|0.05|0.06|0.02|100|1207700|59827.00|47|0|0.00|0|0.05|0|0.00|0.00||N|N|||N||||||||||||||120000000|2020-07-16|7200000.00|THB|THEOAVAEU708||"""

result = convert_string_to_df(string_data)



""" 5. Function """

# 1. verify the input parameter 
def double_number(number):
    if not isinstance(number, int):
        print("my_function is take only int input")
        return None
    else:
        return number * 2
    
# should not modify other(input,global varible) that not given by input (side-effect)
# if pass list or dict make sure to make a copy


# 2. test a function by assert 
assert double_number(2) == 4, "Correct is 4"

# 3. Rules
'''
    1. access only local variable
    2. return all function output (explicit return None)
    3. be aware not to modify other thing unintention
    4. usually does one thing

'''

""" 6. Modules """

# check all search path for this file
import sys
for place in sys.path:
    print(place)

# temporarily append search path
sys.path.append("/Users/nanthawat/Documents/GitHub/AnanCapital/Python/Data")

# Set path (not temporarily)
'''
    1. add __init__.py in folder that contain function
    2. set in terminal: export PYTHONPATH="/path/to/mypackage"
    
    e.g 
    1. add __init_.py in Indicator that contain a file with many indicator 
    2. set in terminal: export PYTHONPATH="/Users/nanthawat/Documents/GitHub/AnanCapital/Python/Indicator"

'''
# import module
from random_data import arbitrary_timeseries
from random_data import generate_trendy_price

arbitrary_timeseries(generate_trendy_price(Nlength=180, Tlength=30, Xamplitude=40.0, Volscale=0.15)).plot()

""" 7. Class """

"""
    When to use class
    1. want to import function and use it in the context of some data
    - use when need to pass a lots of data argument or need to call many function given the same parameter data
"""
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + "."

a = Quote("Ananchim", "Never give up")
a.who()


""" 8. Files and IO """

"""
    - file are simple kind of persistent storage or a collection of data on secondary storage : test vs binary file
    - file is stored in directory or a folder
            
    Type
        1. Text file  (commonly)
        - encoded as "ASCII text" 
        - end a line with "\n"
        - non-printing: tab "\t" , space "\s"
    
    e.g.
        - csv file: columns seperated by either ( , or a tab)
        
    Path    
        - Path: a string that locate a file in the directory: absolute -top lvel or relative - to cwd
        - cwd is the directory that it started from.

"""

# find directory path 
import os
os.getcwd()
os.path.exists("indicator.py")

# list all file in the same directory witg
os.listdir(os.getcwd())

# Open a file and read 
csv_file = "/Users/nanthawat/Desktop/Personal_doc/OAQ_1SampleFile/astsec.csv"
csv_data = pd.read_csv(csv_file)

# may use pickle to store the state of a variable and pick up when needed
import pickle
t1 = [1,2,3]
t2 = pickle.dumps(t1)
t3 = pickle.loads(t2)


""" 9. Except handling """

# fix a missing dict key
word_list = ['rock', 'paper', 'scissors', 'paper']
word_count = dict()

for word in word_list:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1


for word in word_count:
    print( 'Word: %s Count: %s' % (word, word_count[word]))



""" 10. Code Best practice """

"""
    Aspect of code quality
        1.Commenting (explain what and why) and documentation (purpose, limitation, required parameter, side affect, assumption, return)
        2. Variable and function naming
        3. Code organization: avoid repetition x 3!, use function, (use function, class, modules and good code layout),
        
    Summarize
        1. function: calc_something
        2. filename: random_data_generator
        3. constant: CONSTANT
        
    Readmore:
        - PEP8
        
        
"""
# Arithmatic operation
income = (1200
          + 200
          - 300)



""" 11. Algorithm Complexity """

"""
    - Describe scaling behaviour: how much does runtime grow if the size of input grow by a certain factor
    
    Big-O notation
    
    - O(f(n)) meas a function grows in worst case at the rate of f(n) for large enough n
    
        e.g.
        - n^2 - 2n is O(n^2)
        - 100n is O(n)
        -10^12 is O(1)
        
    * for any sorting algo that use pair-wise comparison need nlog(n) in the worst case.
    * The computational complexity and memory is a major deterinant of data structure and algorithm for any application.    
        
"""


""" 12. Design Algorithm """


"""
    Algorithm design paradigms refer to general approaches or strategies used in designing efficient algorithms to solve optimization and search problems.

    Framework
    1. Dynamic programming
    - Dynamic programming is a technique used to solve problems by breaking them down into smaller overlapping subproblems. 
    - It is particularly useful for optimization problems where the solution can be expressed as a combination of optimal solutions to subproblems.
    
    2. DNA pairwise sequence alignment
    - Dynamic programming is commonly applied to solve DNA sequence alignment problems.
    - The algorithm breaks down the problem into smaller subproblems, where each subproblem corresponds to aligning a substring of the DNA sequences. 
    - The optimal alignment is then determined by combining the optimal solutions to these subproblems.
    
    Overall, dynamic programming is a powerful algorithm design paradigm that finds applications in various fields, including DNA sequence alignment.
    It enables the efficient solution of complex problems by breaking them down into smaller overlapping subproblems and storing intermediate results for reuse.

"""




























