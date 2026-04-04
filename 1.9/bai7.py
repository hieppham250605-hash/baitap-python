_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

_new = []
for x in _list:
    if _list.count(x) == 1:
        _new.append(x)

print(_new)