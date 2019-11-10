from nltk.corpus import wordnet
if __name__== '__main__':
    word=(raw_input())
    syns = wordnet.synsets(word)
    a=set()
    i=[]
    b=set()
    for x in syns:
        a.add((x.lemmas()[0].name().encode('ascii','ignore')).lower())
    for x in a:
        b.add(len(x))
    for x in a:
        o=len(x)
        if(o in b):
            print(x)
            b.remove(o) 
