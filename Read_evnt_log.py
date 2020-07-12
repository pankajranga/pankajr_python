import matplotlib.pyplot as plt
import os.path as fpath
names = []
values = []
while(1):
	file1 = open ('D:\learn_stuff\python\eventfile.log','r') # Open the eventfile for readonly
	file_lines = file1.readlines()   # Read the eventlog file line-by-line
	for line in file_lines:
			names.append(line.split(',')[0])
			values.append(int(line.split(',')[1]))
	file1.close()
	# Plot the bar-graph using matplotlib
	plt.bar(names, values,color=['black', 'red', 'green', 'blue', 'cyan'])
	plt.axis([names[0],names[-1],0,50])
	plt.show(block=False)	
	# Clear the plot area to refresh new values
	plt.pause(1)
	plt.clf()
	# Re-initialize the lists
	names = []
	values = []
	# Check if lock file present to continue running reader program.
	if (fpath.isfile('D:\learn_stuff\python\semaphore_file.txt')):
		continue
	else:
		break
	
	

