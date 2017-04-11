import sys
import collections
import os
import operator
# import re # used if needed to remove any non-alphanumeric characters in a word

# theses flag variables determine user flag from sys.argv passed in
wordSorted = False
countSorted = False
anySorted = False

# wordList will hold the words of each file
wordList = list()

def handleArgs():
	# accessing global variables
	global wordSorted
	global countSorted
	global anySorted

	# verifying user input using sys.argv
	if len(sys.argv) == 1:
		print('No arguments provided, program exiting.')
		sys.exit()
	elif len(sys.argv) == 2 and sys.argv[1].startswith('-'):
		print('No files given, program exiting.')
		sys.exit()
	# sys.argv[0] holds the name of the file
	# sys.argv[1] holds the first argument passed in by the user
	if sys.argv[1] == '-w': # first argument
		wordSorted = True
	elif sys.argv[1] == '-c': # first argument
		#print('CountSorted detected.')
		countSorted = True
	elif sys.argv[1].startswith('-') and not (sys.argv[1]=='-w') and not(sys.argv[1]=='-c'): # user entered -X (any) flag.
		#print('Invalid flag, program exiting.')
		sys.exit()
	elif not(sys.argv[1].startswith('-')): # if no flag was entered
		#print('Sorting in any order.')
		anySorted = True
	else:
		print('Unknown error occurred.') # weird stuff happend
		sys.exit()

def processFiles():
	# using global flag
	global anySorted

	# getting the amount of files passed in by user
	files = len(sys.argv) # argv[0] holds file name and argv[1] contains sorting flag
	if anySorted == True:
		#print('Sorting with no flags.')
		files = range(1,files) # no flags, then the filename is in first position
	else:
		#print('Sorting with ' + str(sys.argv[1]) + ' flag.')
		files = range(2,files)# with flags, then the filename is in second position
	
	for file in files: # process each file in the argv
		
		print('Opening ' + str(sys.argv[file]))
		try:
			with open(sys.argv[file], 'r') as f:
				data = f.readlines()# read all lines into data
				for line in data:
					getWords(line) # get the words for each line read
				finalize()# output the results
		except:
			print('file ', str(sys.argv[file]), ' does not exist.')

def getWords(data):
	#print(data.split(' '))
	global wordList # use global wordList
	cursor = 0
	data = data.rsplit('\t')# remove tabs
	data = ';wf;'.join(data)
	data = data.rsplit(' ')# remove spaces
	data = ';wf;'.join(data)
	data = data.rsplit('\n')# remove end lines
	data = ';wf;'.join(data)# join with ;wf; to simplify word seperation
	
	data = data.rsplit(';wf;')# getting all words into data
	
	for word in data:
		if not(word == ''):
			# word = re.sub(r'\W+', '', word) # used to remove non-alphanumeric characers
			
			# removing ending punctuation
			word = word.strip(',')
			word = word.strip(';')
			word = word.strip('.')
			word = word.strip('?')
			word = word.strip('!')
			wordList.append(word.lower())# adding each word to the word list
	
def processWords():
	# using global wordList
	global wordList
	results = dict()# results dictionary
	
	# adding each word and frequency to dictionary
	for word in wordList:
		if word in results.keys():
			results[word] += 1
		else:
			results[word] = 1
	return results
	

	
def finalize():
	results = processWords() # process found words into dictionary
		
	# print out the results for each file based on user provided
	# input/flags and files.
	try:
		if wordSorted:
			# alphabetical order by word
			for key, value in sorted(results.items(), key = operator.itemgetter(0)):
				print(key,' : ', value)
		elif countSorted:
		
			# descending order sort by frequency
			for key, value in sorted(results.items(), key = operator.itemgetter(1),reverse=True):
				print(key,' : ', value)
		else:
			# no order
			for key in results:
				print(key,' : ', results[key])
	except:
		# invalid/un-printable character
		# happens when unicode char/code is in file
		# this is not a program error but an evironment
		# "issue"
		pass
			
	wordList = list()
	
def main():
	handleArgs()
	print('Processing files...')
	processFiles()
	
if __name__ == '__main__':
	main()
	sys.exit()

#example:
	# python files.py filename1.txt filename2.txt filename3.txt
