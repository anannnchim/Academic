#!/usr/bin/env python3
# -*- coding: utf-8 -*-



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

'''

""" 6. Modules """









