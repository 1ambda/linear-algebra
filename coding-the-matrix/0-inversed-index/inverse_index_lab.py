# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.


from random import randint


## 1: (Task 1) Movie Review
def movie_review(name):
    text = ["See it!", "A gem!", "Ideological claprap!"]
    return text[randint(0, len(text)-1)]


## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    inversedIndex = {}
    for index, text in enumerate(strlist):
        for word in text.split():
            if word in inversedIndex:
                inversedIndex[word] |= {index}
            else:
                inversedIndex[word] = {index}

    return inversedIndex


## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    indices = set()

    for q in query:
        indices |= inverseIndex[q]

    return indices


## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    xs = []

    for q in query:
        xs.append(inverseIndex[q])

    return set.intersection(*xs)
