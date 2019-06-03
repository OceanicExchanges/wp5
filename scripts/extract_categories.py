import os
import sys
import json as json
import urllib.request
import operator

backend = sys.argv[1]
annotation_file = sys.argv[2]
query_term = sys.argv[3]
min_count = int(sys.argv[4])
show_every_x = int(sys.argv[5])
translate = sys.argv[6]
merge_words = sys.argv[7:]
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

def readAnnotations(annotation_file):
    annotations = {}
    
    for l in open(annotation_file):
        ls = l.strip().split("\t")
        a1 = ""
        a2 = ""
        w = ls[0]
        if len(ls)>=2:
            a1 = ls[1]
        if len(ls)>=3:
            a2 = ls[2]
        
        if a1==a2:
            annotations[w]=a1
        elif a1=="" and not a2 == "":
            annotations[w]=a2
        elif a2=="" and not a1 == "":
            annotations[w]=a1
        else:
            annotations[w]=a1
    return annotations

[mwd,mwd_rev]=readMergeWords(merge_words)
origin2en = readTranslations(translate)
annotations = readAnnotations(annotation_file)
print(annotations)
url = "%s/track/%s?aggWFParam=1&aggWeighFunction=Gaussian&aggWordsPerYear=5&aggYearsInInterval=5&algorithm=Non-adaptive&boostMethod=Sum+similarity&doCleaning=No&endKey=&forwards=Forward&maxRelatedTerms=10&maxTerms=15&minSim=0.1&startKey=&wordBoost=1"%(backend,query_term)
page = urllib.request.urlopen(url)
content = (page.read())
js = json.loads(content)
vocab = []
vocab_c = {}
data = {}

categories = sorted(list(set(annotations.values())))
categories.append("other")
print("\t".join(categories))

line_en = ""
line = "year"

#print(line_en)
#print(line)
i = -1
for year in js["vocabs"]:
    i+=1
    if i%show_every_x !=0:
        continue
    
    line= "%s"%(year)
    annos = {k:0 for k in categories}

    for w in js["vocabs"][year]:
        for wi,sim in js["vocabs"][year][w]:
            if wi.endswith(","):
                wi=wi.replace(",","")
            if wi in mwd_rev:
                wi = mwd_rev[wi]
            if wi in origin2en:
                wi_en = origin2en[wi]
                if wi_en in annotations:
                    annos[annotations[wi_en]]+=1
                else:
                    print(wi_en)
                    annos["other"]+=1
            else:
                print("Not in translation dict: "+wi)
    for w,c in annos.items():
        line+="\t%d"%(c)
    print(line)

