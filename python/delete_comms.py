txt=open("example.py","r")
lines=txt.readlines()
txt.close()
for line in lines:
	if "#" in line:
		l=line.strip()
		if l[0]!="#": 
			temp=line.split("#")
			count1=tmp[0].count("'")
			count2=tmp[0].count('"')
			if count1%2==1 or count2%2==1:
				print line
			else:
				print line.split("#")[0]
	else:
		print line