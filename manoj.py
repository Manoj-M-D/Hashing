import hashlib
def func(string):

	result = hashlib.md5(string.encode())
	print("The hash code is : \n", end ="")
	print(result.hexdigest())

string = input('enter your name :\n')
func(string)





