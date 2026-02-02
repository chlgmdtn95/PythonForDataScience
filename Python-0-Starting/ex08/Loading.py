import os

def forPrint(i:int, t:int) :
	ret = ""
	for _ in range(i-1):
		ret += "="

	ret+=">"
	if i == t-1 :
		print(f"\r100%|", end="")
	else :
		print(f"\r {i * 100//t }%|", end="")
	print(f"{ret}", end="")

def ft_tqdm(lst: range) -> None :
	for i in range (len(lst)) :
		yield	forPrint(i, len(lst))
