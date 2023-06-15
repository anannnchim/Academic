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


# make list of list
n = 4
k = 3
C = [[0] * (n+1) for i in range(k+1)]


10//11

# get middle
a_list = [5, 2, 9, 4,1, 7, 4]

def get_middle(my_list):
    sorted_list = sorted(my_list)
    return sorted_list[len(sorted_list) // 2]

get_middle(a_list)


# find element
def find_element(sequence, target):
    '''
    Returns the index of the target element in the sequence. 
    If the target is not found, returns -1.
    '''
    if len(sequence) == 0:
        return -1

    x = 0 # index
    while x < len(sequence):
        if sequence[x] == target:
            return x
        x += 1

    return -1  # element not found


# slice as a pair
seq = (2, 0, -2, 2)
wsize = 2
n = len(seq)

for i in range(n - wsize + 1):
    window = seq[i:i+wsize]
    print(window)

# recursive: unnest list
def unnest(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(unnest(element))  # Recursively unnest the nested list
        else:
            result.append(element)  # Add non-list elements to the result list
    return result

# count consec
def count_consecutive(seq, var):
    count = 0
    max_count = 0
    
    for elem in seq:
        if elem == var:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count


# count same 
def count_same_as_previous(seq):
    count = 0
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
    return count



# count diff
def count_same_as_different(seq):
    count = 0
    for i in range(1, len(seq)):
        if seq[i] != seq[i - 1]:
            count += 1
    return count




""" 2. Tuple : unmutable """

myTuple = ("A","B")

""" 3. Dict (HashMap) : no order """

'''
keys(): Returns a view object of all the keys in the dictionary.
values(): Returns a view object of all the values in the dictionary.
items(): Returns a view object of all the key-value pairs in the dictionary as tuples.
get(key): Returns the value associated with the given key. If the key is not found, it returns None (or a default value provided as the second argument).
pop(key): Removes the key-value pair with the specified key from the dictionary and returns the corresponding value.
update(other_dict): Updates the dictionary by adding key-value pairs from another dictionary or an iterable of key-value pairs.
clear(): Removes all the key-value pairs from the dictionary, making it empty.
copy(): Returns a shallow copy of the dictionary.
len(): return number of pairs
'''

 # create a dict
myDict = {"A": 1, "B": 2, "C" : 3, "D" : 3}

# create a dict from list
wordlist = ["test", "your", "ability"]
wordDict = {word : len(word) for word in wordlist}

# set
wordset = set(wordlist)
type(wordDict)

myDict.keys()
myDict.values()
myDict.items()


# add 
myDict.update({'D': '4'})  # Add a key-value pair
myDict['key'] = 'value'  # Add a key-value pair

# remove
myDict.pop("A")

# remove last item
myDict.popitem()

# check element

'b' in {'a' : '01', 'b' : '02', 'c' : '03' }

# check value 
'01' in {'a' : '01', 'b' : '02', 'c' : '03' }.values()




# count thing in dict
def count_dict(my_dict):
    count = dict()
    for elem in my_dict:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1
    return count

count_dict(myDict)



# loop over dict
myDict

for key in myDict.keys():
    print(key)

for item in myDict.items():
    key, value = item
    print(key, value)



# check if invertible 
def is_invertible(adict):
    return len(adict) == len(set(adict.values()))


# count the different    
def count_dict_difference(A, B):
    difference = {}
    
    for key in A:
        if key in B:
            count_diff = A[key] - B[key]
            if count_diff > 0:
                difference[key] = count_diff
        else:
            difference[key] = A[key]
    
    return difference

""" 4. String """

# strip, replace 
myString = "Nanthawat Anan?   "
myString.strip("?")
myString.replace("Anan", "Chim")
myString.strip()
myString + str(12)
myString.replace("a", "01")

# count 
myString.count("an")


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
    5. Put assertion on pre-condition. (input)
    6. Put assertion on post condition. (ouput)

'''


# test case for function

# Write at most four test cases for this function. For each test case, you must write down the input (argument to the function) and the expected return value. Your test cases should cover all relevant corner cases.
def smallest_non_negative(number_list):
    
    '''
    Argument is a list of numeric values (integer or float).
    Returns the smallest non-negative value in the list,
    and zero if there is no such value.'''

    '''
Test Case 1:

Input: [4, 2, 9, -3, 0]
Expected Output: 0
Explanation: This test case checks the function's ability to correctly identify 0 as the smallest non-negative number in the list.

Test Case 2:

Input: [3.2, 2.9, 2.1, -1.2, -0.5]
Expected Output: 2.1
Explanation: This test case checks the function's ability to handle float numbers and correctly identify 2.1 as the smallest non-negative number.
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


# car example
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("The car engine is starting.")
    
    def drive(self):
        print(f"Driving the {self.make} {self.model}.")
    
    def get_age(self, current_year):
        age = current_year - self.year
        return age

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Calling instance methods
my_car.start_engine()
my_car.drive()

# Calling the get_age method
current_year = 2023
car_age = my_car.get_age(current_year)
print(f"The car is {car_age} years old.")



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
        - the overall amount of memory or space utilized by algorithm
        - for any sorting algo that use pair-wise comparison need nlog(n) in the worst case.
        - The computational complexity and memory is a major deterinant of data structure and algorithm for any application.    
        - Space complextity = Auxiliary(temporary memory) + space used by input value
    
    
    Big-O notation

        - O(f(n)) meas a function grows in worst case at the rate of f(n) for large enough n
    
        e.g.
        - n^2 - 2n is O(n^2)
        - 100n is O(n)
        -10^12 is O(1)
        * look at the fastest growing term.
        
        
    Calculating Complexity (examine it line by line on each following factors)
        1. Assignment, bits and math operators are all basic operations.
        2. loop and nested loop.
        3. recursion and function invocations.
        
        - ignore constant. 
        
    
        
"""

# Following are the key time and space complexities:
'''
    1. Constant: O(1)
    2. Linear time: O(n)
    3. Logarithmic time: O(n log n)
    4. Quadratic time: O(n^2)
    5. Exponential time: 2 ^(n)
ุุุ    6. Factorial time: O(n!)
'''
    

# 1. Constant: O(1) - no dependence on the input size n.
def constant_time(list_data):
    print(list_data)  # algo require one execution
    
# 2. Linear: O(n) - run time increase linearly with the length of input or iterates over size of n.
def linear_time(list_data, size ):
    for i in range(size): # depend on size n
        print(i, list_data[i]) 
 
# 3. Logarithm: O(log n) - when size of input data decrease each step by a certain factor. As input size grow the number of execute grows compareatively much slower.
def binary_search(list_data, value):
    '''
    Binary search is a method that takes a sorted list and searches through it for the value.
    '''
    
    # Pointers
    low = 0
    high = len(list_data) - 1
    
    # Repeat until the pointers low and high meet each other
    while low <= high: # Hence, every iteration, the size of the search list shrinks by half
        mid = (low + high) // 2  # Calculate the midpoint index
        
        if list_data[mid] == value:
            return mid
        
        elif list_data[mid] < value:
            low = mid + 1 
        
        else:
            high = mid - 1 
    
    return -1

# 4. Quadratic time: O(n^2) - time related to the squared size of input (increase expo), e.g. several iterate through data sets. (nested loop)
def quadratic_time(list_data, size):
    for i in range(size):
        for j in range(size): # Hence, run n time j or n^2
            print("Iteration : " ,i, "index j " ,j, " is ", list_data[j]) 


# 5. Expoential time: O(2^n) - when n is increased by one, number of execution is double
def fibonacci(n):
    if(n <= 1):
        return 1
    else:
        return fibonacci(n - 2) + fibonacci( n - 1)  # recursive 




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


""" 13. Except handling (MAY 16) """

'''
    Kind of Error:
        1. Syntax: grammar 
        2. Sematic: run good but fail to do what I expect
        3. Runtime: not enough memory, can't find file
        
    
    Error Handling:
        1. case 1,2: fix bug and make program stop. we don't want code to be robust for bug.
        - use: assertion, and kill the program, throw an exception
        
        2. case 3: find a root and if we did not find, find other root
        - e.g. ask input, if user give it wrong, ask again.
        
            Solution:
                1. return distinguished value such as Nan
                2. return tuple (normal value, exception)
                3. throw exception: try catch, raise 
                * Exception is (type classes) that inherit from Exception.
                
'''


""" 14. Unit testing """
'''
    Terms:
        - Unit testing: a function that check if a function work correctly
        - System-level testing: usually for scientific pipeline, use real small data that already know the truth and verify the result
            
    Unit testing (for detect bugs)
        1. Specify the assumption: test pre-condition input e.g. (pre-condition = input is number, test should not be string since it is not pre-condition)
        2. identify test cases (edges case) e.g. boundary condition 
        3. verify behavior on return value each case
        
'''

""" 15. classes """




# Create a list
my_list = [1, 2, 3]

# Use the extend method to add multiple elements to the list
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Use the append method to add a single element to the end of the list
my_list.append(7)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7]

# Use the insert method to insert an element at a specific index
my_list.insert(0, 0)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7]

# Use the sort method to sort the elements in ascending order
my_list.sort()
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7]

# Use the pop method to remove and return an element at a specific index
popped_element = my_list.pop(1)
print(popped_element)  # Output: 1
print(my_list)  # Output: [0, 2, 3, 4, 5, 6, 7]

# Use the remove method to remove the first occurrence of a specific value
my_list.remove(3)
print(my_list)  # Output: [0, 2, 4, 5, 6, 7]

# Use the reverse method to reverse the order of the elements in the list
my_list.reverse()
print(my_list)  # Output: [7, 6, 5, 4, 2, 0]





# Create a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Use the keys method to get a list of all keys in the dictionary
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# Use the values method to get a list of all values in the dictionary
values = my_dict.values()
print(values)  # Output: dict_values(['John', 30, 'New York'])

# Use the items method to get a list of key-value pairs in the dictionary
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Use the get method to retrieve the value associated with a key
age = my_dict.get("age")
print(age)  # Output: 30

# Use the pop method to remove and return the value associated with a key
city = my_dict.pop("city")
print(city)  # Output: 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30}

# Use the update method to merge another dictionary into the current dictionary
other_dict = {"country": "USA", "occupation": "Engineer"}
my_dict.update(other_dict)
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'country': 'USA', 'occupation': 'Engineer'}





# Create a set
my_set = {1, 2, 3, 4, 5}

# Use the add method to add an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Use the remove method to remove an element from the set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Use the union method to create a new set that is the union of two sets
other_set = {4, 5, 6, 7, 8}
union_set = my_set.union(other_set)
print(union_set)  # Output: {1, 2, 4, 5, 6, 7, 8}

# Use the intersection method to create a new set that is the intersection of two sets
intersection_set = my_set.intersection(other_set)
print(intersection_set)  # Output: {4, 5, 6}

# Use the difference method to create a new set that contains elements in one set but not the other
difference_set = my_set.difference(other_set)
print(difference_set)  # Output: {1, 2}

# Use the issubset method to check if one set is a subset of another set
subset = {1, 2}
print(subset.issubset(my_set))  # Output: True

# Use the issuperset method to check if one set is a superset of another set
superset = {1, 2, 3, 4, 5, 6, 7}
print(superset.issuperset(my_set))  # Output: True
