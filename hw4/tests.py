from skc2143_hw4 import *

print('-------------------------------')
print('       Problem 1      ')
print('-------------------------------')

print('Output: ' + los('abcd'))
print('Expect: abcd')
print('Output: ' + los('xabcyz'))
print('Expect: abcyz')
print('Output: ' + los('cba'))
print('Expect: c')
print('Output: ' + los('larry'))
print('Expect: ar')
print('Output: ' + los('xabcxabcdexuvwxyz'))
print('Expect: abcdex')

print('-------------------------------')
print('       Problem 2      ')
print('-------------------------------')
print('Output: %s' %([c2f(0), c2f(100), f2c(32), f2c(212)]))
print('Expected: [32.0, 212.0, 0.0, 100.0]')

print('-------------------------------')
c = Constraint('C F', [9,-5], -5*32)
print(c.setvar(0, 100))
print(c.setvar('F', 212))

print('-------------------------------')
print('       Problem 3      ')
print('-------------------------------')
v2a = [10,20]
v2b = [0, 1]
v3a = [1,3,-5]
v3b = [-2, 4, 1]
v4a = range(1,6)
v4b = [1,0,1,0,1]
output = [mindot(v2a,v2b),mindot(v3a, v3b), mindot(v4a, v4b)]
print(output)

print('-------------------------------')
print('       Problem 4      ')
print('-------------------------------')
cash1 = 4
prices1 = [1,1,1,1,8]
cash2 = 200
prices2 = [150, 24, 79, 50, 88, 345, 3]
cash3 = 8
prices3 = [2, 1, 9, 4, 4, 56, 90, 3]
cash4 = 542
prices4 = [230, 863, 916, 585, 981, 404, 316, 785,
88, 12, 70, 435, 384, 778, 887, 755, 740,
337, 86, 92, 325, 422, 815, 650, 920, 125,
277, 336, 221, 847, 168, 23, 677, 61, 400,
136, 874, 363, 394, 199, 863, 997, 794, 587,
124, 321, 212, 957, 764, 173, 314, 422, 927,
783, 930, 282, 306, 506, 44, 926, 691, 568,
68, 730, 933, 737, 531, 180, 414, 751, 28,
546, 60, 371, 493, 370, 527, 387, 43, 541,
13, 457, 328, 227, 652, 365, 430, 803, 59,
858, 538, 427, 583, 368, 375, 173, 809, 896,
370, 789]

result = [pickitems(prices1, cash1), pickitems(prices2, cash2), pickitems(prices3, cash3), pickitems(prices4, cash4)]
print(result)

print('-------------------------------')
print('       Problem 5      ')
print('-------------------------------')
@secure
def foo(a, b):
	return (a + b)
@secure
def bar(a, b=34):
	return(a+b)

#foo(1,2)
#foo('frank', 'bad', 1 ,2)

#foo('jack', 'nope')

print(foo('jack', 'jackpw', 1 ,2))
print(bar('jill', 'jillpw', 5, b = 35))
