import sys 

def main():
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	else:
		name='nobody'
	print " Hello " + name
	
	
if __name__=='__main__':
	main()
  
