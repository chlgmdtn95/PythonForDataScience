import sys

def main() :
	NESTED_MORSE = {
		" ": "/",
		"A": ".-",
		"B": "-...",
		"C": "-.-.",
		"D": "-..",
		"E": ".",
		"F": "..-.",
		"G": "--.",
		"H": "....",
		"I": "..",
		"J": ".---",
		"K": "-.-",
		"L": ".-..",
		"M": "--",
		"N": "-.",
		"O": "---",
		"P": ".--.",
		"Q": "--.-",
		"R": ".-.",
		"S": "...",
		"T": "-",
		"U": "..-",
		"V": "...-",
		"W": ".--",
		"X": "-..-",
		"Y": "-.--",
		"Z": "--..",
		"1": ".----",
		"2": "..---",
		"3": "...--",
		"4": "....-",
		"5": ".....",
		"6": "-....",
		"7": "--...",
		"8": "---..",
		"9": "----.",
		"0": "------"
	}
	try :
		ret = ""
		assert len(sys.argv) == 2
		for i in (sys.argv[1]).split():
			assert i.isalnum()

		for i in range(len(sys.argv[1])) :
			if i != 0:
				ret += " "
			ret += NESTED_MORSE[sys.argv[1][i].upper()]
		print(ret)

	except AssertionError :
		print("AssertionError: the arguments are bad")

if __name__ == "__main__" :
	main()