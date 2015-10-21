"""
Steve Cheruiyot -- skc2143
Python w3103 - Homework 4
Oct 20, 2015
"""

from itertools import * 
from operator import *

"""
Problem 1 - Longest Ordered Substring(los)
@param str input string
@return longest ordered substring of str
"""
def los(str):
	result = str[0:1]
	stringList = []
	for i in range(1, len(str)):
		if str[i] > str[i - 1]:
			result += str[i]
		else:
			stringList.append(result)
			result = str[i]
	stringList.append(result)

	strlen = 0
	longest = ''
	for j in stringList:
		if len(j) > strlen:
			strlen = len(j)
			longest = j

	return longest

"""
Problem 2
Conversion between Celsius and Fahrenheit, using the equation 9C = 5(F-32)
"""
# Celsius to Fahrenheit
def c2f(celsius):
	return float(9 * celsius / 5) + 32

# Fahrenheit to Celsius
def f2c(farhenheit):
	return float(5 / 9) * (farhenheit - 32)

# Constraint class
class Constraint:
	"""
	Setup constraint btw C and F
	@param names
	@param coefficients
	@param total
	"""
	def __init__(self, names, coefficients, total):
		self.names = {}
		self.variables = names.split(' ')
		self.coefficients = coefficients		
		self.total = total
		self.count = len(self.variables)

	"""
	setvar will fire when there is only one unset variable remaining it will 
	print the variable values, and returns them in a list, and clear all
	variable values
	@param arg variable index or name
	@param value variable value
	"""
	def setvar(self, arg, value):
		if type(arg) is int:
			self.names[self.variables[arg]] = value
		else:
			self.names[arg] = value
		self.count -= 1
		if self.count == 1:
			i = 0
			result = 0
			for k in self.names:
				result += self.names[k] * self.coefficients[i]
				i += 1
			self.names[self.variables[-1]] = (self.total - result) / self.coefficients[-1]
			
			outputList = []
			for j in self.names:
				print('%s = %s' %(j, self.names[j]))
				outputList.append(self.names[j])
			self.names = {}
			self.count = len(self.variables)
			return outputList

"""
Problem 3
Finds the minimum of all possible dot products when the order of vectors is permuted
@param vectorA vector
@param vectorB vector of same length as vectorA
@return minimum dot product
"""
def mindot(vectorA, vectorB):
	permutationA = list(permutations(vectorA, len(vectorA)))
	permutationB = list(permutations(vectorB, len(vectorB)))
	minDotProduct = 2**64
	for i in range(0, len(permutationA)):
		for j in range(i, len(permutationB)):
			dotProduct = sum(map(mul, list(permutationA[i]), list(permutationB[j])))
			if dotProduct < minDotProduct:
				minDotProduct = dotProduct
	return minDotProduct

"""
Problem 4
@param prices list of prices for things in a store
@param cash amount of cash
@return list of prices that exactly spend cash
"""
def pickitems(prices, cash):
	for i in range(1, len(prices)):
		result = list(combinations(prices, i))
		for j in result:
			if sum(j) == cash:
				return list(j)

"""
Problem 5
Function decorator
"""
class secure(object):
	"""Adds two required arguments before others, a 'user' and a 'password'"""
	def __init__(self, f):
		self.f = f
		self.up = {}
		self.up['jack'] = 'jackpw'
		self.up['jill'] = 'jillpw'

	"""
	@param user user's name
	@param pw password
	"""
	def __call__(self, user, pw, *pos, **kw):
		if not user in self.up:
			raise Exception('User %s not registered' % user)
		if pw != self.up[user]:
			raise Exception('Wrong password')
		return self.f(*pos, **kw)