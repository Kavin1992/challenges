from data import DICTIONARY, LETTER_SCORES
from test_wordvalue import TestWordValue

def load_words():
	"""Load dictionary into a list and return list"""
	with open('dictionary','r') as f:
		return f.readlines()

def calc_word_value(word):
	"""Calculate the value of the word entered into function
	using imported constant mapping LETTER_SCORES"""
	return reduce(lambda x,y:x+y,[LETTER_SCORES[i.upper] for i in word])

def max_word_value(words):
	"""Calculate the word with the max value, can receive a list
	of words as arg, if none provided uses default DICTIONARY"""
	if words=='':
		res=[(i,calc_word_value(i)) for i in load_words()]
	else:
		res = [(i, calc_word_value(i)) for i in words]
	return sorted(res,key=lambda x:x[1])

if __name__ == "__main__":
	tst=TestWordValue()
    tst.
	pass # run unittests to validate
