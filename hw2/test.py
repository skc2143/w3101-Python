from skc2143_hw2 import *
'''
print(list(decimals(125)))

print(list(genlimit(decimals(3), 5)))
print(list(genlimit(decimals(8), 5)))


print(select(range(5), [0, 1, '', "foo", True]))

print([nbitIntToDigits(3, 2), nbitIntToDigits(3, 6), nbitIntToDigits(11, 4)])


for entry in powerSet(['avery', 'math', 'butler', 'dodge']):
	print(entry)

print(countBases('CATCGATATCTCTGAGTGCAC'))

print(reverseComplement('ACGT'))

path = './oil.txt'
g = oil(path)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
'''
for j in range(2, 30):
	d = list(decimals2(j))
	print(' Expansion of 1/' + str(j) + ':')
	print(d)