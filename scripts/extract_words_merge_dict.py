import os
import sys
import json as json
import urllib.request
import operator

backend = sys.argv[1]
query_term = sys.argv[2]
min_count = int(sys.argv[3])
show_every_x = int(sys.argv[4])
translate = sys.argv[5]
merge_words = sys.argv[6:]
def readMergeWords(merge_words):
    mwd = {}
    mwd_rev = {}
    for mw in merge_words:
        word= mw[:mw.find(":")]
        words = mw[mw.find(":")+1:].split(",")
        mwd[word]=set(words)
        for w in words:
            mwd_rev[w]=word
        mwd_rev[word]=word
    return [mwd,mwd_rev]

def readTranslations(translate):
    origin2en={}
    for l in open(translate):
        ls = l.strip().split("\t")
        origin2en[ls[0]]=ls[1]
    return origin2en

[mwd,mwd_rev]=readMergeWords(merge_words)
origin2en = readTranslations(translate)

url = "%s/track/%s?aggWFParam=1&aggWeighFunction=Gaussian&aggWordsPerYear=5&aggYearsInInterval=5&algorithm=Non-adaptive&boostMethod=Sum+similarity&doCleaning=No&endKey=&forwards=Forward&maxRelatedTerms=10&maxTerms=15&minSim=0.1&startKey=&wordBoost=1"%(backend,query_term)
print(url)
page = urllib.request.urlopen(url)
content = (page.read())
js = json.loads(content)
vocab = []
vocab_c = {}
data = {}
for year in js["vocabs"]:
    data[year]={}
    for w in js["vocabs"][year]:
        for wi,sim in js["vocabs"][year][w]:
            if wi ==w and sim == 0.0:
                continue
            if wi in mwd_rev:
                wi = mwd_rev[wi]
            if wi not in vocab:
                vocab.append(wi)
                vocab_c[wi]=0
            if wi not in data[year]:
                data[year][wi]=[]
            data[year][wi].append(sim)
            vocab_c[wi]+=1

sorted_x = sorted(vocab_c.items(), key=operator.itemgetter(1),reverse =True)
line_en = ""
line = "year"

for (w,c) in sorted_x:
    if c>min_count:
        line+="\t%s(%d)"%(w,c)
        line_en+="\t"+origin2en.get(w,"UNKNOWN")
print(line_en)
print(line)
i = -1
for year in data:
    i+=1
    if i%show_every_x !=0:
        continue
    line= "%s"%(year)
    for (w,c) in sorted_x:
        if c<=min_count:
            continue
        if w in data[year]:
            line+="\t%.4f"%(float(sum(data[year][w]))/len(data[year][w]))
        else:
            line+="\t%.4f"%(0.0)

    print(line)
