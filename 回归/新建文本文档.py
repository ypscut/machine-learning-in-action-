f=open('ex0.txt')
stock=[]
for line in f.readlines():
	line=line.replace('\t','\n')
	stock.append(line)
f.close()
print stock
