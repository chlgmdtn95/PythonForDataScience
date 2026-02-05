from os import get_terminal_size

def forPrint(i:int, t:int) :
	terminal_width = tuple(get_terminal_size())[0]

	left_ret = f"{i * 100 // t :>3}%|".rjust(5)
	# right_ret = f"| {i}/{t} [00:01<00:00, 196.50it/s]"
	right_ret = f"| {i}/{t}                          "
	loading_bar_len = int((i / t) * (terminal_width - len(left_ret) - len(right_ret)))
	mid_ret = "█" * loading_bar_len
	mid_ret += " " * (terminal_width - len(left_ret) -len(right_ret) - loading_bar_len)

	ret = left_ret + mid_ret + right_ret
	print(f"\r{ret}", end="", flush=True)

def ft_tqdm(lst: range) -> None :
	for i in range (len(lst)) :
		forPrint(i, len(lst))
		yield lst[i]
	forPrint(len(lst), len(lst))
