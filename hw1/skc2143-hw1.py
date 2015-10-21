# Steve Cheruiyot -- skc2143
# COMS W3101 Homework 1

# Problem 1a
def dp(v1, v2):
    length = min(len(v1), len(v2))
    dotProduct = 0
    for i in range(0, length):
        dotProduct += v1[i] * v2[i]
    return dotProduct;

# Problem 1b
def shortlong(v1, v2):
	return [v1, len(v1), v2, len(v2)]

# Problem 1c
def odp(v1, v2, offset):
    length = min(len(v1), len(v2))
    dotProduct = 0
    for i in range(0, length):
        dotProduct += v1[i] * v2[i + offset] if len(v1) < len(v2) else v1[i + offset] * v2[i]
    return dotProduct;

# Problem 1d
def pdp(v1, v2, pad):
    length = max(len(v1), len(v2))
    a = [] + v1
    b = [] + v2
    if len(v1) < len(v2):
        a.extend([pad] * (length - len(v1)))
    else:
        b.extend([pad] * (length - len(v2)))
    dotProduct = 0
    for i in range(0, length):
        dotProduct += a[i] * b[i]
    return dotProduct;

# Problem 2
def rle(input):
    runLength = []
    counter = 1
    current = input[0]
    for i in range(1, len(input)):
        if input[i] == current:
            counter += 1
        else:
            runLength.append([current, counter])
            current = input[i]
            counter = 1
            if i == len(input) - 1:
                runLength.append([current, counter])
    return runLength

# Problem 3
def partition(l, n, overlap):
    partitions = []
    i = 0
    while i <= len(l) - n:
        partitions.append(l[i:i + n])
        i += n - overlap
    return partitions

# Problem 4a
def expandlazy(input):
    if isinstance(input, range) or isinstance(input, zip) or isinstance(input, enumerate):
        return list(input)
    else:
        return input

# Problem 4b
def expandlazylist(input):
    output = []
    for i in range(0, len(input)):
        if isinstance(input[i], range) or isinstance(input[i], zip) or isinstance(input[i], enumerate):
            output.append(list(input[i]))
        else:
            output.append(input[i])
    return output

# Problem 5
def flatten(input):
    if input == []:
        return input
    if isinstance(input[0], list):
        return flatten(input[0]) + flatten(input[1:])
    return input[:1] + flatten(input[1:])