a = [['петя',10,130,35], ['вася',11,135,39],
['женя',9,140,33],['дима',10,128,30]]

n = input('Сортировать по имени (1),возрасту (2), росту (3), весу (4): ')
n = int(n)-1

def sort_col(i):
    return i[n]

a.sort(key=sort_col)

print(a)
'''for i in a:
    print("%7s %3d %4d %3d" % (i[0],i[1],i[2],i[3]))'''