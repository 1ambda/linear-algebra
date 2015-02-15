# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.


## 1: (Problem 1) Tuple Sum
def tuple_sum(A, B):
    xs = []

    for i in range(len(A)):
        xs.append((A[i][0]+B[i][0], A[i][1]+B[i][1]))

    return xs


## 2: (Problem 2) Inverse Dictionary
def inv_dict(d):
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Examples:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'})
    {'merci':'thank you', 'au revoir':'goodbye'}]
    '''
    dic = {}

    for k in d.keys():
        v = d[k]
        dic[v] = k

    return dic


## 3: (Problem 3) Nested Comprehension
def row(p, n):
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    xs = []

    for i in range(n):
        xs.append(p + i)

    return xs


comprehension_with_row = [row(i, 20) for i in range(15)]
comprehension_without_row = [[i+j for j in range(20)] for i in range(15)]


## 4: (Problem 4) Probability Exercise 1
Pr_f_is_even = 0.7
Pr_f_is_odd  = 0.3


## 5: (Problem 5) Probability Exercise 2
Pr_g_is_1    = 0.4
Pr_g_is_0or2 = 0.6

