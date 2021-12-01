txt = open("P&P.txt", encoding="latin-1").read().split()
#txt = open("text.txt", encoding="latin-1").read().split()
import random


##1a) by dictionary
freq = {}
def word_counts(w):
    global freq
    for i in range(len(txt)):
        if txt[i] in freq.keys():
            count = freq.get(txt[i])
            count += 1
            freq[txt[i]] = count
        else:
            freq[txt[i]] = 1
    return (freq.get(w))

    #generate dic, ask wha count
    #for word in text


##1b)
def top10(L):
    max10 = []
    for i in range(10):
        maximum = max(L)
        max10.append(maximum)
        L.remove(maximum)
    return max10



##1c)
def top10_words(L):
    global freq
    get_freq = word_counts("a")
    #don't use the variable, just need to run word_counts to get freq dictionary
    top_ten = []

    freq = {y:x for x,y in freq.items()} #replaces words that are said the same amount of times

    #create inverse dic, one list per dic index

    in_order = sorted(freq.items())

    for i in range(10): #range(10)
        top_ten.append(in_order[len(in_order)-1-i][1])

    return top_ten

##2 Done -> desktop, b) change the wording in textfile ~+~

##3a
def search(keyword):


    import urllib.request
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p="+keyword)
    page = f.read().decode("utf-8")
    f.close()

    #with open("text.txt", 'r') as f:
        #page = f.read()

    list = page.split()

    abt_index = list.index('lh-22">About') #string search : string.find
    if list[abt_index+2] == "search":
        return(list[abt_index+1])

##3b
def choose_variant(variants):
    res = {}
    for i in range(len(variants)):
        res[i] = search(variants[i])
    res = {y:x for x,y in res.items()}
    res = sorted(res.items())
    res = max(res)
    res = res[1]

    return variants[res]



if __name__ == "__main__":
    #print(word_counts("man."))


    # L = random.sample(range(1, 1000), 100)
    # print(top10(L))
    #
    # #print(top10_words(freq))

    print(search("engineeringscience"))

    print(choose_variant(["five-yearanniversary", "fifthanniversary"]))
    print(choose_variant(["toprankedschooluoft", "toprankedschoolwaterloo"]))









