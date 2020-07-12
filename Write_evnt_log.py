from random import seed
from random import randint
import time
import os
seed(1)
file_str=''
# Create a locking file for the reader program to continue running till this lock file is present
semaphore_file = open('D:\learn_stuff\python\semaphore_file.txt','w')
semaphore_file.close()
# Start a ticker, for this example I have used 20.
for tic in range (20):
	# Create a list of some random events
	event_lst = [['evnt_1','evnt_2','evnt_3','evnt_4','evnt_5','evnt_6','evnt_7','evnt_8','evnt_9'], [randint(2,50) for x in range(10)]] # Create a list of some random events
	# Write the events in eventlog file
	with open ('D:\learn_stuff\python\eventfile.log','w') as f:
		for y in range (len(event_lst[0])):
			file_str = event_lst[0][y] + ',' + str(event_lst[1][y]) + '\n'
			f.write(file_str)
	f.close()
	time.sleep(2)

os.remove('D:\learn_stuff\python\semaphore_file.txt')
