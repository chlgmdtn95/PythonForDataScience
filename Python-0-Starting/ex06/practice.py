# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# squared_list = [n**2 for row in arr for n in row]
# flat_one = [[n for n in row] for row in arr]
# print(squared_list)
# print(flat_one)

lists = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]

def test(t):
    assert type(t) is int, '정수 아닌 값이 있네'

for i in lists:
    test(i)