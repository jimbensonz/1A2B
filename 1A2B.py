import random

NUMBER_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Guess:
	def __init__(self):
		self.lst = [Pos(0), Pos(1), Pos(2), Pos(3)]

	def update(self, guess, a, b):
		if a == 0 and b == 0:
			for i in range(4):
				self.lst[0].delCdt(guess[i])
				self.lst[1].delCdt(guess[i])
				self.lst[2].delCdt(guess[i])
				self.lst[3].delCdt(guess[i])
		elif a == 0:
			self.lst[0].delCdt(guess[0])
			self.lst[1].delCdt(guess[1])
			self.lst[2].delCdt(guess[2])
			self.lst[3].delCdt(guess[3])
		elif a+b == 4:
			self.lst[0].candidate = intersection(guess, self.lst[0].candidate)
			self.lst[1].candidate = intersection(guess, self.lst[1].candidate)
			self.lst[2].candidate = intersection(guess, self.lst[2].candidate)
			self.lst[3].candidate = intersection(guess, self.lst[3].candidate)

	def guessing(self):
		ret = []
		ret.append(self.lst[0].guessing(ret))
		ret.append(self.lst[1].guessing(ret))
		ret.append(self.lst[2].guessing(ret))
		ret.append(self.lst[3].guessing(ret))
		return ret

class Pos:
	def __init__(self, idx=0, value=0):
		self.idx = idx
		self.value = value
		self.candidate = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	def delCdt(self, num):
		n = int(num)
		if n in self.candidate:
			self.candidate.remove(n)

	def guessing(self, black_lst):
		return random.choice([x for x in self.candidate if x not in black_lst])

class BruteForce:
	def __init__(self):
		self.TOTAL_LIST = []
		for a in range(10):
			for b in range(10):
				for c in range(10):
					for d in range(10):
						buf = [a, b, c, d]
						if len(set(buf)) == 4:
							self.TOTAL_LIST.append(buf)

	def update(self, guess, a, b):
		self.TOTAL_LIST = [x for x in self.TOTAL_LIST if self.match(x, guess, a, b)]

	def guessing(self):
		return random.choice(self.TOTAL_LIST)

	def match(self, x, guess, a, b):
		score = evaluate(''.join(map(str, x)), guess)
		return score[0] == a and score[1] == b

def intersection(lst1, lst2):
	return list(set(lst1) & set(lst2))

def verify_valid_input(s):
	if not s.isdigit():
		print('Invalid input! Please enter 4 digits.')
		return False
	if not len(s) == 4:
		print('Invalid input! Please enter 4 digits.')
		return False
	return True

def verify_answer(ans, guess=''):
	return str(ans) == str(''.join(map(str, guess)))

def evaluate(ans, guess):
	s = 0
	for g in guess:
		if str(g) in ans:
			s = s + 1
	for idx in range(len(guess)):
		if ans[idx] == str(guess[idx]):
			s = s + 9
	return int(s / 10), s % 10



ans = input('Enter your number: ')
while(not verify_valid_input(ans)):
	ans = input('Enter your number again: ')

print('')
print('')
print('')
print('=============================')
print('')
print('Computer start guessing!')
print('')
print('=============================')
print('')
print('')
print('')


count = 0
guess = ''
score = (0, 0)
game = Guess()

while(not score[0] == 4 or not score[1] == 0):
	count = count + 1
	print('Round ', count)
	guess = game.guessing()
	print('Guess: ', guess)
	score = evaluate(ans, guess)
	print(score[0], 'A', score[1], 'B')
	game.update(guess, score[0], score[1])


print('')
print('===============================')
print('')
print('The answer is ', guess)
print('Total trial: ', count)
print('')
print('')



count = 0
guess = ''
score = (0, 0)
game = BruteForce()
while(not score[0] == 4 or not score[1] == 0):
	count = count + 1
	print('Round ', count)
	guess = game.guessing()
	print('Guess: ', guess)
	score = evaluate(ans, guess)
	print(score[0], 'A', score[1], 'B')
	game.update(guess, score[0], score[1])
	print('Length: ', len(game.TOTAL_LIST))

print('')
print('===============================')
print('')
print('The answer is ', guess)
print('Total trial: ', count)
print('')
print('')
