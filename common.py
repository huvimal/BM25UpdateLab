"""Small deterministic experimental utilities, copied into each standalone project."""
import hashlib
import json
import re
import time
import numpy as np

MODEL_PROVENANCE=[]

def wordset(text):return set(re.findall(r'\w+',text.casefold()))
def retrieval_docs():
    return ['reset password account authentication','restore backup database snapshot','free disk storage capacity',
            'restart worker queue jobs','renew certificate tls expiration','trace packet network timeout',
            'clear cache stale records','rebuild index search documents']

def bm25_scores(docs,query):
    vocab=bow_fit(docs);matrix=bow(docs,vocab);q=bow([query],vocab)[0];length=matrix.sum(1);df=(matrix>0).sum(0)
    idf=np.log(1+(len(docs)-df+.5)/(df+.5))
    return (((matrix*2.2)/(matrix+1.2*(.25+.75*length[:,None]/max(1e-9,length.mean()))+1e-12))*idf*q).sum(1)

def rng(seed=42): return np.random.default_rng(seed)
def sigmoid(x): return 1/(1+np.exp(-np.clip(x,-30,30)))
def fit(x,y,steps=350,rate=.15,weights=None):
    x=np.c_[np.ones(len(x)),x]; w=np.zeros(x.shape[1]);weights=np.ones(len(y)) if weights is None else weights
    for _ in range(steps): w-=rate*x.T@((sigmoid(x@w)-y)*weights)/len(y)
    return w
def probability(x,w):return sigmoid(np.c_[np.ones(len(x)),x]@w)
def measures(y,p,t=.5):
    pred=p>=t;truth=np.asarray(y,dtype=bool)
    tp=int(sum(pred&truth));fp=int(sum(pred&~truth));fn=int(sum(~pred&truth))
    precision=tp/max(1,tp+fp);recall=tp/max(1,tp+fn)
    order=np.argsort(-np.asarray(p),kind='stable');sorted_y=truth[order];pr=np.cumsum(sorted_y)/np.arange(1,len(y)+1)
    return {'accuracy':float(np.mean(pred==truth)),'precision':precision,'recall':recall,
            'f1':2*precision*recall/max(1e-12,precision+recall),'average_precision':float(sum(pr*sorted_y)/max(1,sum(truth))),
            'fp':fp,'fn':fn,'cases':len(y)}
def classification(seed=7,n=900,d=8):
    r=rng(seed);x=r.normal(size=(n,d));y=(x[:,0]+.7*x[:,1]-.4*x[:,2]+r.normal(0,.7,n)>0).astype(float)
    return x[:500],y[:500],x[500:700],y[500:700],x[700:],y[700:]
def normalize(x):return x/np.maximum(np.linalg.norm(x,axis=-1,keepdims=True),1e-12)
def softmax(x):
    z=x-np.max(x,axis=-1,keepdims=True);e=np.exp(z);return e/e.sum(axis=-1,keepdims=True)
def fingerprint(value):return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def bow_fit(texts):return {w:i for i,w in enumerate(sorted(set(re.findall(r'\w+',' '.join(texts).lower()))))}
def bow(texts,vocab):
    a=np.zeros((len(texts),len(vocab)))
    for row,text in enumerate(texts):
        for w in re.findall(r'\w+',text.lower()):
            if w in vocab:a[row,vocab[w]]+=1
    return a
def timed(fn,repeats=5):
    fn();dur=[]
    for _ in range(repeats):
        start=time.perf_counter();fn();dur.append(time.perf_counter()-start)
    return float(np.median(dur))
def check(condition,message):
    if not condition:raise AssertionError(message)
    return message

