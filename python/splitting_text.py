import random

txt=open("example.txt","r")
init=txt.read()
words=init.split()
a=(len(words))
while(len(words)>2):
	a=random.randint(0,len(words)-4)
	print (words[a-1],words[a],words[a+1])
	del (words[a-1],words[a],words[a+1])