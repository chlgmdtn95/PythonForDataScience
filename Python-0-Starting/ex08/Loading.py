from os import get_terminal_size

def forPrint(i:int, t:int) :
	terminal_width = tuple(get_terminal_size())[0]
	one_col = "█" * ((terminal_width - 30 - ((2 * len(str(t))))) // t)
	one_blank = " " * ((terminal_width - 30 - ((2 * len(str(t))))) // t)
	ret = ""
	for _ in range(i):
		ret += one_col
	for _ in range(t-i, 0, -1):
		ret += one_blank
	ret += f"| {i}/{t}"
	print(f"\r{i * 100//t :>3}%|".rjust(5), f"{ret}", end="", sep='', flush=True)

def ft_tqdm(lst: range) -> None :
	for i in range (len(lst)) :
		forPrint(i, len(lst))
		yield lst[i]
	forPrint(len(lst), len(lst))
