import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return cosine similarity between sparse vectors vec1 and vec2, stored as dictionaries.'''
    dot_prod = 0
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            if list(vec1.keys())[i] == list(vec2.keys())[j]:
                dot_prod += list(vec1.values())[i] * list(vec2.values())[j]
    
    return dot_prod / (norm(vec1) * norm(vec2))

print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))

def build_semantic_descriptors(sentences):
    '''Return a dictionary d such that for every word w that appears in at least one of 
    the sentences, d[w] is itself a dictionary which represents the semantic descriptor of w'''
    dictionary = {}

def build_semantic_descriptors_from_files(filenames):
    pass



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass