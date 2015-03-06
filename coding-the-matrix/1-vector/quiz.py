class Vec:
    def __init__(self, domain, function):
        self.D = domain
        self.f = function


def zero_vec(D):
    return Vec(D, {d: 0 for d in D})


def setItem(v, d, val):
    v.f[d] = val


def getItem(v, d):
    return v.f[d] if d in v.f else 0


def list2vec(L):
    return Vec(set(range(len(L))), {k:v for k, v in enumerate(L)})


def list_dot(U, V):
    return sum([u * v for u, v in zip(U, V)])




def test():
    # vec test
    v = Vec({'A', 'B', 'C'}, {'A': 1})
    for d in v.D:
        if d in v.f:
            print(v.f[d])

    # zero_vec test
    D = {'A', 'B', 'C'}
    v = zero_vec(D)
    for d in v.D:
        print(v.f[d])

    # list2vec test
    L = [1, 2, 3, 4]
    V = list2vec(L)

    for d in V.D:
        print(d)
        print(V.f[d])

    # dot_prod test
    U = [1, 2, 3]
    V = [2, 3, 4]
    print(list_dot(U, V))

