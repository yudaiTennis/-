from urllib.request import urlopen
import time
import random
import string
#from itertools import permutations

def query(url):
	res = urlopen(url)
	return res.read()

def create_string():
	strr = "ABCD"
	new_s = ""
	for i in range(0,50):
		new_s += random.choice(strr)
	return new_s

token = "GbGiekaQIthcCiBG30jebneVz95ABHjl"


def score(string):
	strr = string
	url = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, strr)
	result = query(url)
	print(result)

	time.sleep(1)

def permute_string(str):
	if len(str) == 0:
		return ['']
	prev_list = permute_string(str[1:len(str)])
	next_list = []
	for i in range(0,len(prev_list)):
		for j in range(0,len(str)):
			new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
			if new_str not in next_list:
				score(new_str)
				next_list.append(new_str)
	return next_list

if __name__ == "__main__": 
	#for i in range (0,100):
		#strr = create_string()
		#score(strr)
	lst = permute_string(create_string())



#AAABBBABDBCACBBBBCADCACDDDDCBADBACACCBCBDDCCADDDCC