# Importing required modules.
import os

# Defining the function
def linear_search(given_list, key):
	""" Performs Linear Search.
	Args:
		list (list) : to search the key from 
		key (int) : the value to be searched
	Return: 
		index (int) : index position of the key
	"""
	index = -1
	for i in range(len(given_list)):
		if given_list[i] == key:
			index = i
			break
	return index

if __name__ == '__main__':
	# Initializing a list.
	given_list = [1,3,6,2,8,9,4,0,5]
	# Sorting not required in the Linear Search Algorithm.
	# key : the value to be searched.
	key = int(input('Enter the value of the num to be searched: '))
	# Calling the function to perform the Linear Search.
	index = linear_search(given_list, key)
	if index == -1:
		print('Error: value not found!')
	else:
		print("Value you searched is at index: ", index, " in the given list.")