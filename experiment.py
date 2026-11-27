from collections import Counter
import numpy as np
from common import *

class Index:
    def __init__(self):self.docs={};self.df=Counter()
    def add(self,key,text):
        if key in self.docs:self.remove(key)
        self.docs[key]=text;self.df.update(wordset(text))
    def remove(self,key):
        text=self.docs.pop(key);self.df.subtract(wordset(text));self.df+=Counter()
    def search(self,query):
        n=len(self.docs);avg=sum(len(t.split()) for t in self.docs.values())/max(1,n);rows=[]
        for key,text in self.docs.items():
            tf=Counter(text.split());length=len(text.split());score=0
            for word in wordset(query):
                count=tf[word];idf=np.log(1+(n-self.df[word]+.5)/(self.df[word]+.5));score+=idf*count*2.2/(count+1.2*(.25+.75*length/max(avg,1e-9)))
            rows.append((key,float(score)))
        return sorted(rows,key=lambda r:(-r[1],r[0]))
def run():
    inc=Index()
    for i,text in enumerate(retrieval_docs()):inc.add(str(i),text)
    inc.remove('2');inc.add('0','password token account reset');inc.add('8','backup restore password audit')
    full=Index()
    for key,text in inc.docs.items():full.add(key,text)
    query='password backup';a=inc.search(query);b=full.search(query)
    return {'incremental_ranking':a,'document_frequencies':dict(inc.df),
            'checks':[check(inc.df==full.df,'Incremental DF equals clean rebuild'),check(a==b,'Updated BM25 scores match full rebuild exactly')],
            'scope':'Small in-memory BM25 updates with add, replace and delete. Not a concurrent persistent search engine or semantic retriever.'}
