# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
	#if name[0] == 'D':
		#return True
	#if name[0] == 'N':
		#return True
	#else:
		#return False
	#with or
	if name[0]=='D' or name[0]=='N':
	   return True
	else:
	   return False

print is_friend('Dex')
print is_friend('Nancy')
print is_friend('ankit')