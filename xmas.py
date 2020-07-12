def prn_tri(tri_size, tri_fill,start_pos,last):
	next_spc=1;
	for i in range (1,tri_size+1):
	    print (" "*(start_pos+10-(i+2)),"/",tri_fill*next_spc,"\\",sep="")
	    next_spc += 2
	if (last):
		print (" "*(start_pos+10-(i+3)),"*","*"*(next_spc//2),"*","*"*(next_spc//2+1),sep="")
	else:
		print (" "*(start_pos+10-(i+3)),"*","*"*(next_spc//2),chr(581),"*"*(next_spc//2+1),sep="")
for i in range (1,8-1):
	start_pos=25
	if (i == 1):
		print (" "*(start_pos+8),chr(164),sep="")
		print (" "*(start_pos+8),chr(581),sep="")
	if (i % 2):
		prn_tri(i,"@",start_pos,False);
prn_tri(i+1,"@",start_pos,True);

