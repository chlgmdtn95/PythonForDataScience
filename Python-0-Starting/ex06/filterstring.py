import sys
from ft_filter import ft_filter

def main() :
	try:
		assert len(sys.argv) == 3
		in_str = sys.argv[1].split()
		for i in in_str :
			assert i.isalnum()
		assert sys.argv[2].isdigit()

		print(list(ft_filter(lambda n: len(n) > int(sys.argv[2]), in_str)))

	except AssertionError:
		print("AssertionError: the arguments are bad")


if __name__ == "__main__":
	main()