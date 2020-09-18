import random
import os
from termcolor import colored, cprint 

# Data Definition - Variable declaration
os.system('color')
list1=[]
dict_player_names = {}
play_w_comp = 'Y'
first_play = 'Z'
player_name_1 = 'Human'
player_name_2 = 'Computer'

win_pos_dict = {
1: {'pos':[0,1,2],'fill_count':0},
2: {'pos':[3,4,5],'fill_count':0},
3: {'pos':[6,7,8],'fill_count':0},
4: {'pos':[0,3,6],'fill_count':0},
5: {'pos':[1,4,7],'fill_count':0},
6: {'pos':[2,5,8],'fill_count':0},
7: {'pos':[0,4,8],'fill_count':0},
8: {'pos':[2,4,6],'fill_count':0}
}

grid_size = 3

for  x in range (grid_size * grid_size):
	list1.append(x + 1)


#  Input seeking from User to set game mode

while (True):
	play_w_comp = input("Do you want to play with computer [Y/N]: ").upper()
	if (play_w_comp == 'Y' or play_w_comp == 'N'):
		break
	else:
		print("Error!!! Invalid input, please try again")

if (play_w_comp == 'N'):
	player_name_1 = input("Enter name of first player -> ")
	player_name_2 = input("Enter name of second player -> ")
else:
	player_name_1 = input("Enter name of player -> ")

while(True):
	if (play_w_comp == 'N'):
		player_1_char = input("%s , choose your character [ O / X ] -> " %(player_name_1)).upper()
	else:
		player_1_char = input("Choose your character [ O / X ] -> ").upper()
	if (player_1_char == 'O' or player_1_char == 'X' ):
		dict_player_names[player_1_char] = player_name_1	
		break

if (player_1_char == 'O'):
	player_2_char = 'X'
	dict_player_names[player_2_char] = player_name_2
else:
	player_2_char = 'O'
	dict_player_names[player_2_char] = player_name_2

if (play_w_comp == 'Y'):
	print ("Please choose level of difficulty:")
	print ("V. Easy - 1")
	print ("Easy - 2")
	print ("Medium - 3")
	print ("Hard - 4")
	while (True):
		level_of_dif = input("Enter your choice of level: ")
		if (level_of_dif.isnumeric() and int(level_of_dif) in range(1,5)):
			level_of_dif = int(level_of_dif)
			break
		print("Error!! please choose correct level")

	first_play = input ("Press 'C' if you want computer to play first => ").upper()



# Function to print the game grid
	
def prnt_grid():

	print("+-----" * grid_size + "+")
	for i in range(len(list1)):
		if (list1[i] == player_1_char or list1[i] == player_2_char):
			if (list1[i] == player_1_char):
				print("| ",colored(list1[i],'green',attrs = ['reverse']),end="  ")
			else:
				print("| ",colored(list1[i],'magenta',attrs = ['reverse']),end="  ")
		else:
			print("| ",list1[i],end="  ")
		if ((i + 1) % grid_size == 0):
			print("| ")	
			print("+-----" * grid_size + "+")

num_to_zero = 0

print("Original List, see below:")
prnt_grid()

grid_counter = 0
won = 'Z'

def change_player(play_char):
	if (play_char == player_1_char):
		return player_2_char
	else:
		return player_1_char

		
def check_pos_empty(pos):
	if (list1[pos] != player_1_char and list1[pos] != player_2_char):
		return True
	else:
		return False
	
	
def check_pos(play_char,w_or_p):
	
	for i in win_pos_dict:
		fill_count = 0
		pos = 0
		for j in win_pos_dict[i]['pos']:
			if (check_pos_empty(j)):
				pos = j + 1
			else:
				if (list1[j] == play_char):
					fill_count += 1
			#print("fill_count = ",fill_count)
		if (fill_count == 3):
			return play_char
		elif (fill_count == 2 and pos != 0 and w_or_p == 'p'):
			#print ('return pos = ', pos)
			return pos
	
	return 'Z'



def count_win_pos(play_char):
	win_pos_count = 0
	for i in win_pos_dict:
		fill_count = 0
		pos = 0
		for j in win_pos_dict[i]['pos']:
			if (check_pos_empty(j)):
				pos = j + 1
			else:
				if (list1[j] == play_char):
					fill_count += 1
			
		if (fill_count == 2 and pos != 0):
			win_pos_count += 1
			
	#print("Win count = ", win_pos_count)
	return win_pos_count
	
def check_d_pos(play_char):
	tmp_list_val = 0
	pos = 0
	
	for i in range(len(list1)):
		if (check_pos_empty(i)):
			tmp_list_val = list1[i]
			list1[i] = play_char
			if(count_win_pos(play_char) == 2):
				#print("In check_d_pos if count_win_pos")
				pos = check_pos(play_char, 'p')
				list1[i] = tmp_list_val
				return pos
			list1[i] = tmp_list_val
			
	return 'Z'

def chk_corner_pos(play_char):
	if (check_pos_empty(0)):
		return 1
	elif(check_pos_empty(2)):
		return 3
	elif(check_pos_empty(6)):
		return 7
	elif(check_pos_empty(8)):
		return 9
	else:
		return 'Z'

def chk_corner_win_pos(play_char):
	tmp_list_val_1 = 0
	tmp_list_val_2  = 0
	pos = 0
	
	for corner_pos in [0,2,6,8]:
		
		if (check_pos_empty(corner_pos)):
			tmp_list_val_1 = list1[corner_pos]
			list1[corner_pos] = play_char
			pos = check_pos(play_char,'p')
			if (type(pos) != str and pos != 0):
				tmp_list_val_2 = list1[pos - 1]
				list1[pos - 1] = change_player(play_char)
				if(count_win_pos(change_player(play_char)) < 2):
					list1[corner_pos] = tmp_list_val_1
					list1[pos - 1] = tmp_list_val_2
					return corner_pos + 1
				
			list1[corner_pos] = tmp_list_val_1
			if (type(pos) != str):
				list1[pos - 1] = tmp_list_val_2
				
	return 'Z'
	
def computer_play_l1_chk():
	position = check_pos(player_2_char, 'p')
	#print("In level - 1 checks ", player_2_char)
	if (type(position) == str):
		position = random.randint(1,9)
	return position
	
def computer_play_l2_chk():
	#print("In level - 2 checks")
	position = check_pos(player_2_char, 'p')
	if (type(position) == str):
		position = check_pos(player_1_char, 'p')
		if (type(position) == str):
			position = random.randint(1,9)
	return position
			
def computer_play_l3_chk():
	#print("In level - 3 checks")
	position = check_pos(player_2_char, 'p')
	if (type(position) == str):
		position = check_pos(player_1_char, 'p')
		if (type(position) == str):
			position = check_d_pos(player_1_char)
			if (type(position) == str):
				position = random.randint(1,9)
	return position

def computer_play_l4_chk():
	#print("In level - 4 checks")
	position = check_pos(player_2_char, 'p')
	if (type(position) == str):
		position = check_pos(player_1_char, 'p')
		if (type(position) == str):
			position = chk_corner_win_pos(player_2_char)
			if (type(position) == str):
				position = check_d_pos(player_1_char)
				if (type(position) == str):
					if (check_pos_empty(4)): # Check middle position
						position = 5
					else: # Check corner positions
						position = chk_corner_pos(player_2_char)
						if (position == 'Z'):
							position = random.randint(1,9)
	return position
	
def computer_play():
	
	if (level_of_dif == 1):
		position = computer_play_l1_chk()
	elif(level_of_dif == 2):
		position = computer_play_l2_chk()
	elif(level_of_dif == 3):
		position = computer_play_l3_chk()
	else:
		position = computer_play_l4_chk()

	return position

def human_play(play_char):
	valid_num = list(range(1,10))
	while (True):
		position = input("%s, please enter your position : " %(dict_player_names[play_char]))
		if (position.isnumeric()):
			if int(position) in valid_num:
				break
		print("Error!!! Please enter a valid non-occupied position.")
	return int(position)
	
def play_now(play_char):
	global won
	global grid_counter

	while(True):
		if (dict_player_names[play_char] != 'Computer'):
			position = human_play(play_char)
		else:
			position = computer_play()

		if (check_pos_empty(position - 1)): 
			if(dict_player_names[play_char] == 'Computer'):
				print("Position chosen by computer is: ", colored(position,'magenta',attrs=['reverse']))
			list1[position - 1] = play_char
			grid_counter += 1
			won = check_pos(play_char, 'w')
			#print ('won = ', won)
			break
		elif(dict_player_names[play_char] != 'Computer'):
			print("Enter correct position")

if (first_play != 'C'):
	play_char = player_1_char
else:
	play_char = player_2_char
	
while(grid_counter < 9 and won != 'X' and won != 'O'):
	play_now (play_char)
	prnt_grid()
	play_char = change_player(play_char)
		

if (won == 'X' or won == 'O'):
	if (dict_player_names[won] == 'Computer'):
		print("Sorry! you lost, its computer's win.")
	else:
		print("Congratulations,",dict_player_names[won], "you have won.")
else:
	print("It's a draw!")
