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

    for key1 in vec1:
        for key2 in vec2:
            if key1 == key2:
                dot_prod += vec1[key1] * vec2[key2]

    if norm(vec1) != 0 and norm(vec2) != 0:
        return dot_prod / (norm(vec1) * norm(vec2))
    return -1


def build_semantic_descriptors(sentences):
    '''Return a dictionary d such that for every word w that appears in at least one of
    the sentences, d[w] is itself a dictionary which represents the semantic descriptor of w'''
    descriptors = {}
    for sentence in sentences:
        unique_words = set(sentence) # Get rid of duplicate words in a sentence
        for word in unique_words:
            if word not in descriptors:
                descriptors[word] = {} # Make new dictionary
            for i in unique_words: # Inside key
                if i != word:
                    if i in descriptors[word]:
                        descriptors[word][i] += 1
                    else:
                        descriptors[word][i] = 1
    return descriptors


def build_semantic_descriptors_from_files(filenames):
    '''Return a dictionary of the semantic descriptors of all the words in filenames'''
    punctuation = [",", "-", "--", ":", ";", "\n"]
    sentences = []
    for filename in filenames:
        with open(filename, "r", encoding="UTF-8") as f:
            text = f.read().lower()
        
        for punc in punctuation:
            text = text.replace(punc, " ")
        listofsentences = re.split('[?.!]', text) # Split text into sentences

        for i in listofsentences:
            sentences.append(i.split()) # Split sentence into words

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Return the element of <choices> which has the largest semantic similarity to <word>. 
    Return the first choice if similarity cannot be computed'''
    mostsimilarword = choices[0] # Default choice
    mostsimilar = -1

    if word in semantic_descriptors:
        worddesc = semantic_descriptors[word]
        for choice in choices:
            if choice in semantic_descriptors:
                choicedesc = semantic_descriptors[choice]

                similarity = similarity_fn(worddesc, choicedesc)
                if similarity > mostsimilar:
                    mostsimilarword = choice
                    mostsimilar = similarity

    return mostsimilarword


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''Return the percentage of questions on which most_similar_word() guesses the answer correctly'''
    correct = 0

    with open(filename, "r", encoding="latin1") as f:
        tests = f.read().lower().strip("\n").split("\n")

    for test in tests:
        items = test.split() # Split each test into an array containing the words in the test
        question = items[0]
        answer = items[1]
        choices = items[2:]
        if most_similar_word(question, choices, semantic_descriptors, similarity_fn) == answer:
            correct += 1

    return 100 * correct / len(tests)


# Tests
if __name__ == '__main__':
    import timeit

    start = timeit.default_timer()

    descriptors = build_semantic_descriptors_from_files(["War and Peace.txt", "Swann's Way.txt"])
    # print(most_similar_word("authentic", ["genuine", "false"], descriptors, cosine_similarity))

    print(run_similarity_test("Tests.txt", descriptors, cosine_similarity))

    stop = timeit.default_timer()

    print('Time: ', stop - start)  
