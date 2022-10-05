def ordered_count(inp):
    #return [(x,inp.count(x)) for x in set(inp)]
    l = list()
    for i in inp:
        if i not in l:
            l.append(i)
    return [(x, inp.count(x)) for x in l]

a = 'abracadabra'
b = 'Code Wars'


print(ordered_count(a))
