'''
Below is the example of CoNLL-U format 
# sent_id = 1
# text = They buy and sell books.
1   They     they    PRON    PRP    Case=Nom|Number=Plur               2   nsubj   2:nsubj|4:nsubj   _
2   buy      buy     VERB    VBP    Number=Plur|Person=3|Tense=Pres    0   root    0:root            _
3   and      and     CONJ    CC     _                                  4   cc      4:cc              _
4   sell     sell    VERB    VBP    Number=Plur|Person=3|Tense=Pres    2   conj    0:root|2:conj     _
5   books    book    NOUN    NNS    Number=Plur                        2   obj     2:obj|4:obj       SpaceAfter=No
6   .        .       PUNCT   .      _                                  2   punct   2:punct           _

# sent_id = 2
# text = I have no clue.
1   I       I       PRON    PRP   Case=Nom|Number=Sing|Person=1     2   nsubj   _   _
2   have    have    VERB    VBP   Number=Sing|Person=1|Tense=Pres   0   root    _   _
3   no      no      DET     DT    PronType=Neg                      4   det     _   _
4   clue    clue    NOUN    NN    Number=Sing                       2   obj     _   SpaceAfter=No
5   .       .       PUNCT   .     _                                 2   punct   _   _

'''
# import regex
# from collections import defaultdict
# import stanza
# import conllu

class formatCoNLLU: 
    def __init__(self,
        id, 
        word,
        label): 
        self.ID = id
        self.FORM = word 
        self.LEMMA = '_' 
        self.UPOS = '_' # Also XPOS label  
        self.XPOS = label 
        self.FEATS = '_' 
        self.HEAD = '_' 
        self.DEPREL = '_' 
        self.DEPS = '_' 
        self.MISC = '_' 

    # Not sure what I'm doing here 
    def __repr__(self): 
        return {'ID':self.ID,
                'FORM':self.FORM ,
                'XPOS':self.XPOS}

# def isSentence(token): 
#     return False 


# Convert train_set.pos & test_set.pos -> CoNLLU format 
f =  open("./train_set.txt","r") 
data_raw = f.readlines()
f.close()
# myDict = {} 
listSentence = []

for idx,line in enumerate(data_raw): 
    try:
        str,label = line.split()
        a = formatCoNLLU(id=idx,word=str,label=label)
        listSentence.append(a)
        # myDict[idx]=a 
        # myDict[str] = label
    except ValueError:
        continue
        # pass

# for idx,val in enumerate(myDict): 
#     if idx == 5: 
#         break 
#     print(idx, val)


# Train POS Tagging 

# Eval POS on test_set.pos 


