# version code 75eb0ae74c69
coursera = 1
# Please fill out this stencil and submit using the provided submission script.


## 1: (Problem 1) Python Comprehensions: Filtering
def myFilter(L, num):
    return [x for x in L if x % num != 0]


## 2: (Problem 2) Python Comprehensions: Lists of Lists

def my_lists(L):
    return [list(range(1, x+1)) for x in L]


## 3: (Problem 3) Python Comprehensions: Function Composition
def myFunctionComposition(f, g):
    return {k:g[f[k]] for k in f.keys()}


## 4: (Problem 4) Summing numbers in a list
def mySum(L):
    total = 0

    for x in L:
        total += x

    return total


## 5: (Problem 5) Multiplying numbers in a list
def myProduct(L):

    total = 1

    for x in L:
        total *= x

    return total


## 6: (Problem 6) Minimum of a list
def myMin(L):
    current = float('infinity')

    for x in L:
        if x < current:
            current = x

    return current


## 7: (Problem 7) Concatenation of a List
def myConcat(L):
    current = ''

    for s in L:
        current += s

    return current


## 8: (Problem 8) Union of Sets in a List
def myUnion(L):
    current = set()

    for s in L:
        current |= s

    return current


## 9: (Problem 9) Complex Addition Practice
# Each answer should be a Python expression whose value is a complex number.

complex_addition_a = 5+3j
complex_addition_b = 0+1j
complex_addition_c = -1+0.001j 
complex_addition_d = 0.001+9j



## 10: (Problem 10) Combining Complex Operations
#Write a procedure that evaluates ax+b for all elements in L

def transform(a, b, L):
    return [a*x + b for x in L]


## 11: (Problem 11) GF(2) Arithmetic
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0

