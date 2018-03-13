num = input("Enter number of cards:")
l = [True] * num
for i in range (1,num+1):
	for j in range (i,num,i):
		l[j-1]= not l[j-1]
count = 0
for k in range (0,num):
	print l[k],k
	if(l[k] == False):
		count +=1
print count
