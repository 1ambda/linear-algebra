# version code 77ed2409f40d+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.

from operator import add

## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    vd = {}

    for row in strlist:
        fields = row.split()
        name = fields[0]
        votes = list(map(lambda x: int(x), fields[3:]))
        vd[name] = votes

    return vd


## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    length = len(voting_dict[sen_b])
    return sum([voting_dict[sen_a][i] * voting_dict[sen_b][i] for i in range(length)])


## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'
        >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        True
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0], 'd': [-1,0,0], 'e': [1, 0, 0]}
        >>> most_similar('c', vd)
        'd'

    Note that you can (and are encouraged to) re-use your policy_compare procedure.
    """

    similarities = {} 

    for s in voting_dict:
        if s != sen:
            sim = policy_compare(s, sen, voting_dict)
            similarities[s] = sim

    return max(similarities, key=lambda k: similarities[k])


## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,0,0]}
        >>> least_similar('c', vd)
        'b'
    """
    similarities = {} 

    for s in voting_dict:
        if s != sen:
            sim = policy_compare(s, sen, voting_dict)
            similarities[s] = sim

    return min(similarities, key=lambda k: similarities[k])

# f = open('voting_record_dump109.txt')
# vd = create_voting_dict(list(f))
# print(most_similar('Chafee', vd))
# print(least_similar('Santorum', vd))

## 5: (Task 2.12.5) Chafee, Santorum
most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """

    totalSimilarity = 0

    for s in sen_set:
        totalSimilarity += policy_compare(s, sen, voting_dict)
    
    return totalSimilarity / float(len(sen_set))

def find_party(party):
    fileName = 'voting_record_dump109.txt'
    f = open(fileName)
    rows = list(f)

    return [row for row in rows if row.split()[1] == party]


def find_most_avg_senator(voting_dict):
    # senators = sorted(voting_dict, key=voting_dict.get)
    # mid = len(senators) // 2
    # return senators[mid+1]

    avgs = []
    length = len(voting_dict)

    for s1 in voting_dict:
        for s2 in voting_dict:
            if s1 != s2:
                sen_set = voting_dict.keys()
                sen_set -= {s1}
                avgs.append((s1, find_average_similarity(s1, sen_set, voting_dict)))

    avgs = sorted(avgs, key=lambda t:t[1])
    return avgs[len(avgs) - 1]


vd = create_voting_dict(find_party('D'))
most_average_Democrat = find_most_avg_senator(vd) # Biden


## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """

    total = None
    length = len(sen_set)
    
    for sen in sen_set:
        if total is None:
            total = voting_dict[sen]
        else:
            total = list(map(add, voting_dict[sen], total))

    return [score/length for score in total]

vd = create_voting_dict(find_party('D'))
average_Democrat_record = find_average_record(set(vd.keys()), vd)



## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Ravella') or br == ('Ravella', 'Fox-Epstein')
        True
    """

    senators = voting_dict.keys()
    rival = ()
    rivalScore = None

    for s1 in senators:
        for s2 in senators:
            length = len(voting_dict[s2])
            r = (s1, s2)
            s = sum([voting_dict[s1][i] * voting_dict[s2][i] for i in range(length)])
            if rivalScore is None:
                rival = r
                rivalScore = s
            elif s < rivalScore:
                rival = r
                rivalScore = s

    return rival

