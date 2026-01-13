import sys

def countString( string: str):
	arr =[0] * 6 
	arr[0] = len(string)

	for i in range(arr[0]):
		if string[i].isupper() :
			arr[1]+=1
		elif string[i].islower():
			arr[2]+=1
		elif string[i] in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" :
		 	arr[3]+=1
		elif string[i].isspace():
		 	arr[4]+=1
		elif string[i].isdigit():
			arr[5]+=1

	return arr
		

def main() :
	try :
		x = ""
		assert len(sys.argv) <= 2 
		
		try :
			if len(sys.argv) == 1 :
				while True :
					y = input()
					
					if y :
						x += y
					else :
						break
			else :
				result = countString(sys.argv[1])
		except EOFError :
			result = countString(y)

		print(f"The text contains {result[0]} characters:")
		print(f"{result[1]} upper letters")
		print(f"{result[2]} lower letters")
		print(f"{result[3]} punctuation marks")
		print(f"{result[4]} spaces")
		print(f"{result[5]} digits")
	
	except AssertionError as e :
		print("Assertion Error: Too many arguments")


if __name__ == "__main__" :
	main()

