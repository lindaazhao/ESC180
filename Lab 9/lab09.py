filepath = 'C:/Users/linda/OneDrive - University of Toronto/Documents/EngSci 21-22/ESC180 Programming/ESC180/Lab 9/'

# Problem 1 (a)
def word_counts(textfilename):
    '''Return a dictionary containing the number of occurrences of each word found in <textfilename>'''
    words = open(filepath + textfilename, encoding="latin-1").read().replace(".", "")
    # Remove all punctuation, periods replaced in creating words
    words = words.replace(",", "")
    words = words.replace("?", "")
    words = words.replace("!", "")
    words = words.replace(";", "")
    words = words.replace(":", "")
    words = words.split() # Turn into list of words, each word is one element

    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

# Problem 1 (b)
def top10(L):
    '''Return a list of the 10 largest integers in L'''
    top_10 = []
    for i in range(10):
        top_10.append(max(L))
        L.remove(max(L))
    return top_10

# Problem 1 (c)
def top10_freq(freq):
    '''Return the top 10 most frequent words from the dictionary <freq>'''
    inv_freq = {}
    for key, value in freq.items():
        inv_freq[value] = key # Keeps replacing the value at "1"
    
    sorted_inv_freq_list = sorted(inv_freq.items())

    if len(sorted_inv_freq_list) < 10:
        for i in range(10-len(sorted_inv_freq_list)):
            # find what the smallest key in inv_freq is
            # add more words with that same key from freq until sorted_inv_freq_list is 10 elements long
            pass
        
    print(sorted(inv_freq.items()))

if __name__ == '__main__':
    # Problem 1 (a)
    freq = word_counts("text.txt")
    print(freq)
    top10_freq(freq)



    # Problem 2
    print(top10([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))

