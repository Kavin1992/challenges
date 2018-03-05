from data import DICTIONARY, LETTER_SCORES
import test_wordvalue
from functools import reduce
def load_words():
    """Load dictionary into a list and return list"""
    with open('dictionary.txt','r') as f:
        result= [i.strip('\n').replace('-','') for i in f.readlines()]
    return result

def calc_word_value(word):
	"""Calculate the value of the word entered into function
	using imported constant mapping LETTER_SCORES"""
	return int(reduce(lambda x,y:x+y,[LETTER_SCORES[i.upper()] for i in word]))

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    print ('words=',words)
    if words==None:
        res=[(i,calc_word_value(i)) for i in load_words()]
        print('res=',res)
    else:
        res = [(i, calc_word_value(i)) for i in words]
        print('res=', res)
    return sorted(res,key=lambda x:x[1],reverse=True)[0][0]

if __name__ == "__main__":
    tst=test_wordvalue.TestWordValue()
    tst.test_load_words()
    tst.test_calc_word_value()
    tst.test_max_word_value()
    pass # run unittests to validate
