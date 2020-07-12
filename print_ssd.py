import sys
list0 = [[" " if (i in (1,2,3)  and x==1) else "#" for x in range(3)] for i in range(5)]
list1 = [["#" if x==2 else " " for x in range(3)] for i in range(5)]
list2 = [[" " if ((i==1 and x in (0,1)) or (i==3 and x in (1,2))) else "#" for x in range(3)] for i in range(5)]
list3 = [[" " if (i in (1,3) and x in (0,1)) else "#" for x in range(3)] for i in range(5)]
list4 = [[" " if ((i in (3,4) and x in (0,1)) or (i in (0,1) and x==1)) else "#" for x in range(3)] for i in range(5)]
list5 = [[" " if ((i==1 and x in (1,2)) or (i==3 and x in (0,1))) else "#" for x in range(3)] for i in range(5)]
list6 = [[" " if ((i in (0,1)  and x in (1,2)) or (i==3 and x==1)) else "#" for x in range(3)] for i in range(5)]
list7 = [[" " if (i in (1,2,3,4)  and x in (0,1)) else "#" for x in range(3)] for i in range(5)]
list8 = [[" " if (i in (1,3) and x==1) else "#" for x in range(3)] for i in range(5)]
list9 = [[" " if ((i in (3,4)  and x in (0,1)) or (i==1 and x==1)) else "#" for x in range(3)] for i in range(5)]
def prnt_ssd(num_to_print):
	for i in range(5):
		for x in num_to_print:
			if (x=='0'):	
				print (''.join(list0[i]),end="  ",sep=" ")
			elif (x=='1'):
				print (''.join(list1[i]),end="  ",sep=" ")
			elif (x=='2'):
				print (''.join(list2[i]),end="  ",sep=" ")
			elif (x=='3'):
				print (''.join(list3[i]),end="  ",sep=" ")
			elif (x=='4'):
				print (''.join(list4[i]),end="  ",sep=" ")
			elif (x=='5'):
				print (''.join(list5[i]),end="  ",sep=" ")
			elif (x=='6'):
				print (''.join(list6[i]),end="  ",sep=" ")
			elif (x=='7'):
				print (''.join(list7[i]),end="  ",sep=" ")
			elif (x=='8'):
				print (''.join(list8[i]),end="  ",sep=" ")
			else:
				print (''.join(list9[i]),end="  ",sep=" ")
		print()

print ("Enter number: ")
x = ( sys.stdin.readline() )

prnt_ssd(x)
