import csv 

dataPath = 'abc.txt'
f = open(dataPath,'r')
reader = csv.reader(f)
li = []
for line in reader :
	#algorithm
	li.append(line)