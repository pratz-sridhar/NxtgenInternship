import sys
import warnings

from BarChart import *
from FromDB import *

if not sys.warnoptions:
    warnings.simplefilter("ignore")
dict1 = {}  # name of the dictionary with all the keys and values.
dict1 = fromdb()
list1 = []  # a list to store all the keys in the dictionary(the hostnames)
list2 = []  # List to store all the values of the dictionaries
la = []  # This stores all the labels


def seperating():
    number=0
    for i in dict1.keys():
        list1.append(i) #appending all the keys to the list

    for i in dict1.values():#making a list of all the values in the dictionary
        la.append(i)
        for c in i:
            if c.isdigit():
                number=(number*10)+int(c)
        list2.append(number)
        number=0
def operation():
        
    defining(list1,list2,la)
    Plotting()


seperating()
operation()


