# version code ef5291f09f60+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

## 1: (Task 1) Minutes in a Week
minutes_in_week = 60 * 24 * 7

## 2: (Task 2) Remainder
remainder_without_mod = 2304811 - (2304811 // 47) * 47

## 3: (Task 3) Divisibility
divisible_by_3 = (673 + 909) % 3 == 0

## 4: (Task 4) Conditional Expression
x = -9
y = 1/2
expression_val = 1.0

## 5: (Task 5) Squares Set Comprehension
first_five_squares = { x ** 2 for x in {1,2,3,4,5} }

## 6: (Task 6) Powers-of-2 Set Comprehension
first_five_pows_two = { 2 ** x for x in {0, 1, 2, 3, 4} }

## 7: (Task 7) Double comprehension evaluating to nine-element set

X1 = { 1, 2, 3 }
Y1 = { 7, 10, 11 }

## 8: (Task 8) Double comprehension evaluating to five-element set
X2 = { 0.25, 0.5, 1}
Y2 = { 0, 2, 4}

## 9: (Task 9) Set intersection as a comprehension
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { s for s in S for t in T if s == t }

## 10: (Task 10) Average
list_of_numbers = [20, 10, 15, 75]
list_average = sum(list_of_numbers) / len(list_of_numbers)

## 11: (Task 11) Cartesian-product comprehension
# Replace ... with a double list comprehension over ['A','B','C'] and [1,2,3]
cartesian_product = [[c, n] for c in ['A', 'B', 'C'] for n in [1, 2, 3]]

## 12: (Task 12) Sum of numbers in list of list of numbers
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(xs) for xs in LofL])

## 13: (Task 13) Three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(x, y, z) for x in S for y in S for z in S if (x+y+z) == 0]

## 14: (Task 14) Nontrivial three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
exclude_zero_list = [(x, y, z) for x in S for y in S for z in S if (x+y+z) == 0 and not (x == y and y == z)]

## 15: (Task 15) One nontrivial three-element tuple summing to zero
S = {-4, -2, 1, 2, 5, 0}
first_of_tuples_list = [(x, y, z) for x in S for y in S for z in S if (x+y+z) == 0 and not (x == y and y == z)][0]


## 16: (Task 16) List and set differ
example_L = [1, 2, 3, 3]

## 17: (Task 17) Odd numbers
odd_num_list_range = {x for x in range(100) if x % 2 != 0}



## 18: (Task 18) Using range and zip
L = ['A', 'B', 'C', 'D', 'E']
range_and_zip = list(zip(range(5), L))


## 19: (Task 19) Using zip to find elementwise sums
A = [10, 25, 40]
B = [1, 15, 20]
list_sum_zip = [sum(t) for t in zip(A, B)]



## 20: (Task 20) Extracting the value corresponding to key k from each dictionary in a list
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [dic[k] for dic in dlist]


## 21: (Task 21) Extracting the value corresponding to k when it exists
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [dic.get(k, 'NOT PRESENT') for dic in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [dic.get(k, 'NOT PRESENT') for dic in dlist] # <-- as you do here


## 22: (Task 22) A dictionary mapping integers to their squares
square_dict = { x:x**2 for x in range(100) }


## 23: (Task 23) Making the identity function
D = {'red','white','blue'}
identity_dict = { k:k for k in D }


## 24: (Task 24) Mapping integers to their representation over a given base
base = 10
digits = set(range(base))
representation_dict = {(x*base**2 + y*base**1 + z*base**0):(x, y, z) for x in digits for y in digits for z in digits}


## 25: (Task 25) A dictionary mapping names to salaries
id2salary = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = { names[ID]:id2salary[ID] for ID in id2salary }


## 26: (Task 26) Procedure nextInts
def nextInts(L): return [ x + 1 for x in L ]


## 27: (Task 27) Procedure cubes
def cubes(L): return [ x**3 for x in L ] 

## 28: (Task 28) Procedure dict2list
def dict2list(dct, keylist): return [ dct[k] for k in keylist ]

## 29: (Task 29) Procedure list2dict
def list2dict(L, keylist): return { keylist[i] : L[i] for i in range(len(L)) }
