import re

def isInBrackets(i, bounds):
	for b in bounds:
		if b[0] < i < b[1]:
			return True

	return False

class Tree:

	def __init__(self, expr):
		self.expr = expr
		self.oper = None
		self.r = None
		self.l = None
		self.parse()

	def parse(self):
		if len(self.expr) == 0:
			return

		bounds = self.getBracketsBounds(self.expr)
		imps = self.findNotInBrackets('->', self.expr, bounds, 0)
		ors = self.findNotInBrackets('|', self.expr, bounds, 1)
		ands = self.findNotInBrackets('&', self.expr, bounds, 1)
		nots = self.findNotInBrackets('!', self.expr, bounds, 0)

		if imps != -1:
			self.oper = '->'
			self.r = Tree(self.expr[imps + 2:])
			self.l = Tree(self.expr[:imps])
		elif ors != -1:
			self.oper = '|'
			self.r = Tree(self.expr[ors + 1:])
			self.l = Tree(self.expr[:ors])
		elif ands != -1:
			self.oper = '&'
			self.r = Tree(self.expr[ands + 1:])
			self.l = Tree(self.expr[:ands])
		elif nots != -1:
			self.oper = '!'
			self.r = Tree(self.expr[1:])
		elif self.expr[0] == '(' and self.expr[-1] == ")":
			self.expr = self.expr[1:-1]
			self.parse()

	def __str__(self):
		if self.oper in ['->', '|', '&']:
			return "({},{},{})".format(self.oper, self.l, self.r)
		elif self.oper == "!":
			return "(!{})".format(self.r)
		else:
			return self.expr

	def getBracketsBounds(self, expr):
		c = 0
		indexes = []
		bounds = []
		for i in range(len(expr)):
			if expr[i] == '(':
				c += 1
				if c == 1:
					indexes.append(i)
					
			if expr[i] == ')':
				c -= 1
				if c == 0:
					indexes.append(i)
					
		for i in range(0, len(indexes), 2):
			bounds.append([indexes[i], indexes[i + 1]])
			
		return bounds

	def findNotInBrackets(self, oper, expr, bounds, r):

		idxs = [item.start() for item in re.finditer(re.escape(oper), expr)]

		if r:
			idxs.reverse()

		for i in idxs:
			if not isInBrackets(i, bounds):
				return i

		return -1
