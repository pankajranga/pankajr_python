import random
import os
from termcolor import colored, cprint 

os.system('color')

# Data Definition - Variable declaration
sl_dict = {
2:{"txt":"L>23","color":"green","attr":["reverse"]},
9:{"txt":"L>36","color":"green","attr":["reverse"]},
20:{"txt":"L>42","color":"green","attr":["reverse"]},
34:{"txt":"L>72","color":"green","attr":["reverse"]},
43:{"txt":"S<17","color":"red","attr":["reverse"]},
50:{"txt":"S<5","color":"red","attr":["reverse"]},
56:{"txt":"S<8","color":"red","attr":["reverse"]},
62:{"txt":"L>96","color":"green","attr":["reverse"]},
71:{"txt":"L>92","color":"green","attr":["reverse"]},
75:{"txt":"S<49","color":"red","attr":["reverse"]},
84:{"txt":"S<58","color":"red","attr":["reverse"]},
99:{"txt":"S<40","color":"red","attr":["reverse"]}
}

grid_size = 10
pl_1 = chr(4)+chr(4)+chr(4)+chr(4)
pl_2 = chr(5)+chr(5)+chr(5)+chr(5)
pl_12 = chr(4)+chr(4)+chr(5)+chr(5)
pos1=0
pos2=0
pl_name1 = input("Enter name of player 1: ")
pl_name2 = input("Enter name of player 2: ")

## Print game grid

def prnt_grid(player1_pos, player2_pos):
	grd_numbering = 0
	rev_num = False
	print_pos = 0
	
	print("Players: " + pl_name1 + "(" + colored(pl_1,'magenta',attrs=['reverse']) + ")" + " AND " + pl_name2 + "(" + colored(pl_2,'yellow',attrs=['reverse']) + ")" )
	print(colored("+------" * grid_size + "+",'grey'))
	
	for j,i in enumerate(range(100,0,-1)):
		clr='cyan'
		atr=[]
		if (grd_numbering > 9 or rev_num == False):
			grd_numbering = 0

		print_pos = i + grd_numbering
		if print_pos in sl_dict.keys():
			clr = sl_dict[print_pos]['color']
			atr = sl_dict[print_pos]['attr']
			print_pos = sl_dict[print_pos]['txt']
		elif(print_pos == player1_pos and print_pos == player2_pos):
			atr=['reverse']
			print_pos = pl_12
		elif (print_pos == player1_pos):
			clr='magenta'
			atr=['reverse']
			print_pos = pl_1
		elif (print_pos == player2_pos):
			clr='yellow'
			atr=['reverse']
			print_pos = pl_2
		
		print(colored("| ",'grey'),colored(print_pos,clr,attrs=atr),end=" " * (4-len(str(print_pos))))
		if (rev_num):
			grd_numbering += 2
		if ((j + 1) % grid_size == 0):
			grd_numbering = -9
			rev_num = not rev_num
			print(colored("| ",'grey'))	
			print(colored("+------" * grid_size + "+", 'grey'))

def prnt_sl_msg(s_or_l,p_name,pos):
	msg=""
	if (s_or_l == 'S'):
		msg = "Ooch! Snake bite for " + p_name + " to position " + str(pos)
	else:
		msg = "Hurray! " + p_name + " gets to ride the ladder to position " + str(pos)
	return msg

def chk_win(pos, other_pos, p_name):
	if (pos >= 100):
		pos = 100
		if (other_pos == "pos1"):
			#print ("Pos1 position = ", pos1)
			prnt_grid(pos1,pos)
		else:
			print ("Pos2 position = ", pos2)
			prnt_grid(pos,pos2)
		
		print("")
		print("%s has won - congrats" %(p_name))
		print("Thanks for playing. Bye!")
		return True
	else:
		return False

def pre_chk_s_l(p_name,p_pos):
	for i in range(1,7):
		if (p_pos+i) in sl_dict.keys():
			if(sl_dict[p_pos+i]['txt'][0] == 'L'):
				print(p_name + " are you feeling lucky. Lets hope to roll " + colored(i,'green',attrs=['reverse']) +" to catch that ladder." )
				return 'green'
			else:
				print("!!! CAUTION !!! " + p_name + ". Cross your fingers and hope the dice DO NOT roll number " + colored(i,'red',attrs=['reverse']) + " to avoid snake.")
				return 'red'
		

def play_game(player_name,player_symbol,player_pos,player_char,clr):
	global pos1
	global pos2
	msg  = ""
	s_or_l=""
	pos_clr='blue'
	
	print("Its " + player_name + "(" + colored(player_symbol,clr,attrs=['reverse']) + ")"" turn. ",end="")
	
	while (input("Press" + colored(' d ','blue',attrs=['reverse','underline']) + "on keyboard: ") != 'd'):
		print("Wrong Input, press 'd' to roll dice")
		
	
	p = random.randint(1,6)
	player_pos += p
	if (player_pos > 100):
		player_pos = 100
	#msg = " (New position for " + player_name + " is " + str(player_pos) + ")"
	msg = "New position for " + player_name + " is " + str(player_pos)
	if player_pos in sl_dict.keys():
		s_or_l = sl_dict[player_pos]['txt'][0]
		player_pos = int(''.join(filter(lambda i: i.isdigit(),sl_dict[player_pos]['txt'])))
		msg = prnt_sl_msg(s_or_l, player_name,player_pos)
		if (s_or_l == 'S'):
			pos_clr = 'red'
		else:
			pos_clr = 'green'
		
	#print ("Dice roll-out for %s " %player_name,": = ",p,msg,sep="")
	print ("Dice = ",colored(' ' + str(p) + ' ',pos_clr,attrs=['reverse']),sep="")
	print(msg,end="")
	x = input(". Continue - [y/n]: ")
	if (x != 'y'):
		print("Thanks for playing. Bye!")
		return True
	os.system('cls')
	if (player_char == "pos1"):
		pos1 = player_pos
		if (chk_win(pos1,"pos2",player_name)):
			return True
	else:
		pos2 = player_pos
		if (chk_win(pos2,"pos1",player_name)):
			return True
	prnt_grid(pos1,pos2)
	
	
print("			*** START GAME *****")

prnt_grid(pos1,pos2)

while(True):
	msg1 = ""
	msg2 = ""
	s_or_l=""
	if(play_game(pl_name1,pl_1,pos1,"pos1","magenta")):
		break
	if(play_game(pl_name2,pl_2,pos2,"pos2","yellow")):
		break
