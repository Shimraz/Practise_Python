#hello world program using dunders

class String: 

	#Dunder method to initiate object
	def __init__(self,string):
		self.string=string

	#print out string object
	def __repr__(self):   
		return 'Object: {}'.format(self.string)

#driver code
if __name__=='__main__':
	#object creation
	string1=String("Hello World Program using Dunders")
	print(string1)

