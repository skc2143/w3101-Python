from skc2143_hw1 import *

print('Running tests for Homework 1:')

tv0 = [1,2,3]
tv1 = [4,5,6,7,8,9]

print('Problem 1a:\nIN: %s, %s' %(tv0, tv1))
print('OUT: %s\n' %(dp(tv0, tv1)))

print('Problem 1b:\nIN: %s, %s' %(tv0, tv1))
print('OUT: %s' %(shortlong(tv0, tv1)))
print('OUT: %s\n' %(shortlong(tv1, tv0)))

print('Problem 1c:\nIN: %s, %s' %(tv0, tv1))
print('OUT: %s\n' %([odp(tv0, tv1, 0), odp(tv0, tv1, 1), odp(tv0, tv1, 2)]))

print('Problem 1d:\nIN: %s, %s' %(tv0, tv1))
print('OUT: %s\n' %([pdp(tv0, tv1, 0), pdp(tv0, tv1, 1), pdp(tv0, tv1, 2)]))

print('Problem 2: RLE:\nIN: ', [10,10,20,33,33,33,33,10,1,30,30,7])
print('OUT: %s\n' %(rle([10,10,20,33,33,33,33,10,1,30,30,7])))

print('Partition: \nIN: list(range(10)),2,1)')
print('OUT: %s\n' %(partition(list(range(10)),2,1)))
print('IN: list(range(10)),4,3))')
print('OUT: %s\n' %(partition(list(range(10)),4,3)))
print('IN: range(10)),4,3))')
print('OUT: %s\n' %(partition(range(10),4,3))) # fix this doesn't show the last range(6,10)

print('Expand Lazy')
print([expandlazy(range(3)), expandlazy('asdf'), expandlazy(enumerate(['a','b','c']))])

print('\nExpand lazy List')
ll = [1,2,3, range(4), 5, zip([1,2,3], [4,5]), 'asdf', enumerate(['a', 'b', 'c'])]
print(expandlazylist(ll))

print('\nFlatten:')
print(flatten([1,[2,3,4,[5,6,[7,8],9],11]]))
print(flatten([1,2,3,[4,56],[44,55],7,8]))