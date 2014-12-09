from numpy.random import randint
from numpy import zeros

class Game:
	def __init__(self):
		self.rounds = []
		self.throw_number = 0

	def throw_dice(self, kept):
		new = list(randint(1, 6, (5 - len(kept))))
		self.throw_number += 1
		self.dices = kept + new
		return self.dices

	def check_number(self):
		if self.throw_number < 3:
			return False
		else:
			self.rounds.append(self.dices)
			self.throw_number = 0
			return True

	def points(self):
		points = 0
		#Enere til seksere:
		points += sum(self.rounds[0][i] == 1 for i in range(5))
		points += 2*sum(self.rounds[1][i] == 2 for i in range(5))
		points += 3*sum(self.rounds[2][i] == 3 for i in range(5))
		points += 4*sum(self.rounds[3][i] == 4 for i in range(5))
		points += 5*sum(self.rounds[4][i] == 5 for i in range(5))
		points += 6*sum(self.rounds[5][i] == 6 for i in range(5))

		if points >= 42:
			points += 50

		#Ett par
		pair_number = 0
		for i in range(5):
			for j in range(5):
				if i != j and self.rounds[6][i] == self.rounds[6][j] and self.rounds[6][i] > pair_number:
					pair_number = self.rounds[6][i]

		#To par
		


		return points




game = Game()

for i in xrange(0, 50):
	game.throw_dice([])
	game.check_number()


print game.points()





