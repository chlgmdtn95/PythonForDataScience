def ft_filter(f, itr) -> filter :
	"""ft_filter(function or None, iterable) --> list_iterator object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
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
# print(ft_filter.__doc__)