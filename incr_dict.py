def incr_dict(d, t):
	if len(t) == 1:
		if not t[0] in d:
			d[t[0]] = 1
		else:
			if type(d[t[0]]) is int:
				d[t[0]] += 1
			else:
				d[t[0]] = 1
	else:
		if not t[0] in d:
			d[t[0]] = incr_dict({}, t[1:])
		else:
			d[t[0]] = incr_dict(d[t[0]], t[1:])

	return d

dct = {}
incr_dict(dct, ('a', 'b', 'c'))
print dct
incr_dict(dct, ('a', 'b', 'c'))
print dct
incr_dict(dct, ('a', 'b', 'f'))
print dct
incr_dict(dct, ('a', 'r', 'f'))
print dct
incr_dict(dct, ('a', 'z'))
print dct
incr_dict(dct, ('b'))
print dct
incr_dict(dct, ('a', 'r', 'f'))
print dct
incr_dict(dct, ('a', 'b', 'c'))
print dct
incr_dict(dct, ('a', 'b', 'e', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c', 'b', 'c'))
print dct
incr_dict(dct, ('a', 'b', 'e'))
print dct
incr_dict(dct, ('a', 'b', 'e'))
print dct


{
	'a': 
	{
		'r': {'f': 1}, 
		'b': {'c': 2, 'f': 1},
		'z': 1
	}
}