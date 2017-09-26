# tictactoe

A Reinforcement Learning approach to train an agent that plays Tic Tac Toe with python 

*================*
* PYTHON CHEAT SHEET  *
*================*

Curly brackets yok, onun yerine indentation var

someList = []  
someList.append('element')
someList[:]      // make copy of list 

--------arithmetic operations
7 ** 2  == 49
"hello" * 2 == "hellohello" //repeat strings
[1,2] + [3,4] == [1,2,3,4] //join lists
[1,2] * 2 == [1,2,1,2] //repeat list elements

-------conditionals
x == y // compare values
x is y // compare instances

if not a == 1:  // a != 1 , not works like !

if a == 1 and b == 2:
     // do something (when the indentation ends the if also ends
     // and, or keywords

if x in [1,2]:
     // in keyword

if x==1:
     //indentation
elif x==2:
     // else if 
else:
     // something

-------Loops
for prime in [2,3,5,7]:
     //do something indentation style
for x in range(5):
     // x= 1,2,..4
for x in range (3,6,2):
     // x = 3,5 (start, stop, step)
for x in range(1,5):
     //do something
     //else wont run if you 'break' out of while
else:
     print("finished")<

while count <5:
     count+=1
while True:
     count+=1
     if count>5:
          break
while count<5:
     //do something
     //else wont run if you 'break' out of while
else:
     print("finished")

   
----- strings
print("{0},{1}".format('test','test2'))
"Hello world!"[4] == "o"
"Hello world!"[4:7] == "o w" // exclude 7
"Hello world!"[4:-1] == "o world" // -1 from the end 
"Hello world!"[4:] == "o world!" // until the end 
"Hello world!"[4:7:2] == "ow" // extended slice syntax [start:stop:step]
"Hello world!"[::-1] == "!dlrow olleH" // reverse string clever

----- dictionary (map)
*is the same as json object*
phonebook={"John":1,"Jack":2}
phonebook["John"] == 1 

del phonebook["John"]
phonebook.pop["John"] // removes John, returns phonebook, 

for name, number in phonebook.items():
     print("{0}: {1}".format(name,number))

----- functions and classes and modules and packages
def sum(a,b):
     return a + b;
def foo(first, second, third, *therest): 
     print(list(therest)) // therest is type tuple
def bar(first,second,third,**options):
     // can call this bar(1,2,3,action='sum',number='first')
     // and inside the method options.get('action') // returns sum
     

class MyClass:
     variable = "blah"
     def function(self):
          //do something

obj = MyClass()

__init__(self,...) for constructor

import urllib
dir(urllib) // returns the functions implemented by module
help(urllib.urlopen) // details and manual

Each package in Python is a directory which MUST contain a special file called __init__.py
foo/__init__.py
foo/bar.py

import foo.bar // we must use the foo prefix to access bar
from foo import bar //  just use bar, imported it to our namespace   


------ numpy arrays
import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
ones = np.ones(9,)     //1d np array

c = a * b      // [4, 10, 18]
c > 12          // [false, false, true]
c[c>12]       // [18]

----- pandas dataframe
import pandas as pd
df = pd.DataFrame(dictionary)
print(df['column'])     // single bracket returns panda series
print(df[['column']])     // double bracket returns a dataframe
print(df[4:6])     // print rows 4 and 5
print(df[:-4:2])     // [start,end,step] for rows

df.iloc[1]     // get second row based on index
df.loc["AUS"]     //get row based on label


-------generators
yield random.randint(1,40)     // returns a number between 1,40 that is iterable. ( for i in  lottery():  lottery is a function with yield instead of return)

------- functional
from functools import partial

>>> sum = lambda x, y : x + y
>>> sum(3,4)
7


>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>> 
>>> print filter(lambda x: x % 3 == 0, foo)
[18, 9, 24, 12, 27]
>>> 
>>> print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]
>>> 
>>> print reduce(lambda x, y: x + y, foo)
139

def multiply(x,y):
        return x * y
mul2 = partial(multiply,2)            // partial( function,arg1,arg2...) note that arg1 starts from left aka first arg
print(mul2(4))          //8

---------------- closure
def counter(number): 
    def increment():
        nonlocal number     // this makes it possible to modify number (otherwise its read only)
        number+=1
        print(number)
    return increment

count = counter(0)
count()
count()
print (number)     // number is undefined ..closure

