import sys

wordSorted = False
countSorted = False
anySorted = False

wordList = list()

def handleArgs():
	global wordSorted
	global countSorted
	global anySorted

	if len(sys.argv) == 1:
		print('No arguments provided, program exiting.')
		sys.exit()
	# sys.argv[0] holds the name of the file
	# sys.argv[1] holds the first argument passed in by the user
	if sys.argv[1] == '-w': # first argument
		wordSorted = True
	elif sys.argv[1] == '-c': # first argument
		print('CountSorted detected.')
		countSorted = True
	elif sys.argv[1].startswith('-') and not (sys.argv[1]=='-w') and not(sys.argv[1]=='-c'): # user entered -X (any) flag.
		print('Invalid flag, program exiting.')
	elif not(sys.argv[1].startswith('-')): # if no flag was entered
		print('Sorting in any order.')
		anySorted = True
	else:
		print('Unknown error occurred.') # weird stuff happend
		sys.exit()
def processFiles():
	global anySorted

	print('In processFiles method.')
	files = len(sys.argv) # argv[0] holds file name and argv[1] contains sorting flag
	if anySorted == True:
		print('Sorting with no flags.')
		files = range(1,files)
	else:
		print('Sorting with ' + str(sys.argv[1]) + ' flag.')
		files = range(2,files)
	for file in files:
		print('Opening ' + str(sys.argv[file]))
		with open(sys.argv[file], 'r') as f:
			data = f.readline()
			

			#words = getWords(data)
			
			#print(data)
			#print(words)

def getWords(data):
	#print(data.split(' '))
	words = data.rsplit('\n')
		
	print(data)
		
	return words
def main():
	handleArgs()
	print('Processing files.')
	results = processFiles()
		

main()
