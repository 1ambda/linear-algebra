# version code 892eb47785b8+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from GF2 import one


## 1: (Problem 1) Vector Comprehension and Sum
def vec_select(veclist, k):
    vs = [v for v in veclist if v[k] == 0]
    return vs


def vec_sum(veclist, D):
    vecSum = Vec(D, {})

    for v in veclist:
        for d in D:
            vecSum[d] += v[d]

    return vecSum


def vec_select_sum(veclist, k, D):
    vs = vec_select(veclist, k)
    return vec_sum(vs, D)


## 2: (Problem 2) Vector Dictionary
def scale_vecs(vecdict):
    vs = []

    for scalar in vecdict:
        v = vecdict[scalar]
        vs.append(v / scalar)

    return vs


## 3: (Problem 3) Constructing span of given vectors over GF(2)
def GF2_span(D, S):

    vecSet = set({Vec(D, {})})

    for v1 in S:
        for v2 in S:
            vecSet.add(v1)
            vecSet.add(v1 + v2)

    return vecSet


## 4: (Problem 4) Is it a vector space 1
# Answer with a boolean, please.
is_a_vector_space_1 = False 



## 5: (Problem 5) Is it a vector space 2
# Answer with a boolean, please.
is_a_vector_space_2 = True 



## 6: (Problem 6) Is it a vector space 3
# Answer with a boolean, please.
is_a_vector_space_3 = False 



## 7: (Problem 7) Is it a vector space 4
# Answer with a boolean, please.
is_a_vector_space_4a = True
is_a_vector_space_4b = False

