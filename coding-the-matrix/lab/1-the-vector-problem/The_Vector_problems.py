# version code ef5291f09f60+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

from GF2 import one

## 1: (Problem 1) Vector Addition Practice 1
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [p1_v[i] + p1_u[i] for i in range(len(p1_v))]
p1_v_minus_u = [p1_v[i] - p1_u[i] for i in range(len(p1_v))]
p1_three_v_minus_two_u = [3*p1_v[i] - 2*p1_u[i] for i in range(len(p1_v))]


## 2: (Problem 2) Vector Addition Practice 2
p2_v = [2, -1, 5]
p2_u = [-1, 1, 1]
p2_v_plus_u = [p2_v[i] + p2_u[i] for i in range(len(p2_u))]
p2_v_minus_u = [p2_v[i] - p2_u[i] for i in range(len(p2_u))]
p2_two_v_minus_u = [2*p2_v[i] - p2_u[i] for i in range(len(p2_u))]
p2_v_plus_two_u = [p2_v[i] + 2*p2_u[i] for i in range(len(p2_u))]


## 3: (Problem 3) Vector Addition Practice 3
p3_v = [0, one, one]
p3_u = [one, one, one]
p3_vector_sum_1 = [p3_v[i] + p3_u[i] for i in range(len(p3_u))]
p3_vector_sum_2 = [p3_v[i] + p3_u[i] + p3_u[i] for i in range(len(p3_u))]


## 4: (Problem 4) GF2 Vector Addition A
u_0010010 = {'c', 'd', 'e'}
u_0100010 = {'b', 'c', 'd', 'e'}

## 5: (Problem 5) GF2 Vector Addition B
v_0010010 = {'c', 'd'}
v_0100010 = set()

## 6: (Problem 6) Solving Linear Equations over GF(2)

x_gf2 = [0, 1, 1, 1]

## 7: (Problem 7) Formulating Equations using Dot-Product
v1 = [2, 3, -4, 1]
v2 = [1, -5, 2, 0]
v3 = [4, 1, -1, -1]

## 8: (Problem 8) Practice with Dot-Product
uv_a = 5
uv_b = 6
uv_c = 16
uv_d = -1.0
