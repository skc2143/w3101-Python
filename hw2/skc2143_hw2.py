# Steve Cheruiyot -- skc2143
# W3101-Python Homework 2
# Sept 25, 2015

# Problem 1a - decimals
def decimals(d):
	quotient = 1
	while quotient % d is not 0:
		if quotient < d:
			quotient *= 10
		yield(quotient // d)
		quotient = quotient % d

# Problem 1b
def genlimit(g, limit):
	for i in range(0, limit):
		yield(next(g))

# Problem 2 - Dealing with repeated decimals
def decimals2(d):
    repeated = []
    g = decimals(d)
    start = next(g)
    repeated.append(start)
    while True:
        yield(start)
        current = next(g)
        if current == repeated[0]:
            repeated.append(current)
        start = next(g)
        if len(repeated) and repeated[0] == start:
            yield(repeated)
            return
        else:
            yield(current)

# Problem 3a 
def select(l, selectors):
	selected = []
	for i in range(0, len(selectors)):
		if selectors[i]:
			selected.append(l[i])
	return selected

# Problem 3b
def nbitIntToDigits(i, n):
	binary = bin(i)
	binaryList = []
	for i in range(2, len(binary)):
		binaryList.append(int(binary[i]))
	while len(binaryList) is not n:
		binaryList.insert(0, 0)
	return binaryList


# Problem 3c
def powerSet(l):
	powerset = [[]]
	for i in range(0, len(l)):
		for j in range(i + 1, len(l) + 1):
			powerset.append(l[i:j])
	return powerset


# Problem 4 - Decrypting Government Data
# Generator function that summarizes govt data about oil consumption
def oil(path):
    f = open(path)

    for i in range(0, 7):
        next(f)
    
    maximumLeft = 0
    minimumLeft = float('inf')
    maximumRight = 0
    minimumRight = float('inf')

    counter = 0

    for line in f:
        if counter % 14 == 0:
            if counter == 0:
                years = line.split()
                try:
                    data = next(f).split()
                except StopIteration:
                    break
            else:
                data.append(str(maximumLeft))
                data.append(str(minimumLeft))
                data.append(str(maximumRight))
                data.append(str(minimumRight))
                yield(report(years, data, True))
                yield(report(years, data, False))
                years = line.split()
                try:
                    data = next(f).split()
                except StopIteration:
                    break
            counter += 1
        else:
            monthlyData = line.split()
            maximumLeft = float(monthlyData[5]) if float(monthlyData[5]) > maximumLeft else maximumLeft
            minimumLeft = float(monthlyData[5]) if float(monthlyData[5]) < minimumLeft else minimumLeft
            maximumRight = float(monthlyData[12]) if float(monthlyData[12]) > maximumRight else maximumRight
            minimumRight = float(monthlyData[12]) if float(monthlyData[12]) < minimumRight else minimumRight
        counter += 1

# Problem 4 - Helper function for making summary string
def report(years, data, leftside):
    if leftside:
        print('%s: quan: total=%s prices: max = %s min = %s avg = %s' %(years[0], data[1], data[14], data[15], data[5]))
    else:
        print('%s: quan: total=%s prices: max = %s min = %s avg = %s' %(years[1], data[8], data[16], data[17], data[12]))

# Problem 5a
def countBases(dna):
	count = [0, 0, 0, 0]
	for c in dna:
		if c is 'A':
			count[0] += 1
		elif c  is 'C':
			count[1] += 1
		elif c  is 'G':
			count[2] += 1
		elif c  is 'T':
			count[3] += 1
	return count


# Problem 5b
def reverseComplement(dna):
	complement = ''
	for i in range(1, len(dna) + 1):
		if dna[-i] is 'A':
			complement += 'T'
		elif dna[-i] is 'T':
			complement += 'A'
		elif dna[-i] is 'C':
			complement += 'G'
		elif dna[-i] is 'G':
			complement += 'C'
	return complement