class Solution:
	def isValid(self, s: str) -> bool:
		a1 = 0
		a2 = 0
		b1 = 0
		b2 = 0
		c1 = 0
		c2 = 0
		for i in range(s):
			if s[i] == '(':
				a1 += 1
			elif s[i] == ')':
				a2 += 1
			elif s[i] == '[':
				b1 += 1
			elif s[i] == ']':
				b2 += 1
			elif s[i] == '}':
				c1 += 1
			elif s[i] == '{':
				c2 += 1
			return a1 == a2 and b1 == b2 and c1 == c2