def ft_filter(f, itr) -> filter :
	if f is None :
		return iter([n for n in itr if n])
	else :
		return iter([n for n in itr if f(n)])

# print( list(filter(lambda n: n > 6, [5, 7, 0, 500, 304] )))
# print( list(ft_filter(lambda n: n > 6, [5, 7, 0, 500, 304])))

# print( list(filter(None, ['a', 'b', ''])))
# print( list(ft_filter(None, ['a', 'b', ''])))

# print(type(filter(None, [1, 2, 0])))
# print(type(ft_filter(None, [1, 2, 0])))

# print(filter.__doc__)