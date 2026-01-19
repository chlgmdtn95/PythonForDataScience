import sys
from ft_filter import ft_filter

def main() :
	try:
		assert len(sys.argv) < 4
		assert sys.argv[1].isalnum()
		assert sys.argv[2].isdigit()

		print(list(ft_filter(lambda n: len(n) < int(sys.argv[2]), sys.argv[1])))

	except AssertionError:
		print("AssertionError: the arguments are bad")


if __name__ == "__main__":
	main()