import random
import sys
import os
flag= 0
sum=0
numbers_list = []
for x in range(0,30):
	numbers_list.append(random.randint (-30,30))
	print numbers_list

for x in range(0,27):
	sum = numbers_list[x]+ numbers_list[x+1] + numbers_list[x+2]
	if  sum ==0   :
		print  numbers_list[x] , numbers_list[x+1] , numbers_list[x+2]
		flag = 1

if flag == 0 :
	print ("Den brethike tetoios sindiasmos")

