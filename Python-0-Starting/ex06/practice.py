arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

squared_list = [n**2 for row in arr for n in row]
flat_one = [[n for n in row] for row in arr]
print(squared_list)
print(flat_one)