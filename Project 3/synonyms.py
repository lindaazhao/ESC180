import math
import re


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
    if len(vec1) != len(vec2):
        return -1

    for i in range(len(vec1)):
        for j in range(len(vec2)):
            if list(vec1.keys())[i] == list(vec2.keys())[j]:
                dot_prod += list(vec1.values())[i] * list(vec2.values())[j]

    return dot_prod / (norm(vec1) * norm(vec2))

print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))


def build_semantic_descriptors(sentences):
    '''Return a dictionary d such that for every word w that appears in at least one of
    the sentences, d[w] is itself a dictionary which represents the semantic descriptor of w'''
    descriptors = {}
    for sentence in sentences:
        unique_words = set(sentence) # Get rid of duplicate words in a sentence
        for word in unique_words:
            if word not in descriptors:
                descriptors[word] = {}
            for i in unique_words: # Inside key
                if i != word:
                    if i in descriptors[word]:
                        descriptors[word][i] += 1
                    else:
                        descriptors[word][i] = 1
    return descriptors


def build_semantic_descriptors_from_files(filenames):
    punctuation = [",", "-", "--", ":", ";", "\n"]
    sentences = []
    for filename in filenames:
        with open(filename, "r", encoding="UTF-8") as f:
            text = f.read()
            for punc in punctuation:
                text = text.replace(punc, " ")
            listofsentences = re.split('[?.!]', text)

            for i in listofsentences:
                sentences.append(i.split())

    return build_semantic_descriptors(sentences)

some_descriptors = build_semantic_descriptors_from_files(["War and Peace.txt"])
print(some_descriptors["the"])


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Return the element of <choices> which has the largest semantic similarity to <word>'''
    mostsimilarword = ""
    mostsimilar = 0

    worddesc = semantic_descriptors[word]
    for choice in choices:
        choicedesc = semantic_descriptors[choice]

        similarity = similarity_fn(worddesc, choicedesc) 
        if similarity > mostsimilar:
            mostsimilarword = choice
            mostsimilar = similarity
    
    return mostsimilarword



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass