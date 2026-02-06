from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(33)):
	sleep(0.5)
	# print("right after sleep")
print()

for elem in tqdm(range(33)):
	sleep(0.5)
print()
