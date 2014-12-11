from numpy.random import randint
from numpy import zeros

class Game:
	def __init__(self):
		self.rounds = []
		self.throw_number = 0

	def throw_dice(self, kept):
		new = list(randint(1,7, (5 - len(kept))))
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

	def get_points_at_finish(self, verbose):
		points = 0

		#Enere til seksere:
		points += sum(self.rounds[0][i] == 1 for i in range(5))
		if verbose:
			print "Enere: ", sum(self.rounds[0][i] == 1 for i in range(5))

		points += 2*sum(self.rounds[1][i] == 2 for i in range(5))
		if verbose:
			print "Toere: ", 2*sum(self.rounds[1][i] == 2 for i in range(5))

		points += 3*sum(self.rounds[2][i] == 3 for i in range(5))
		if verbose:
			print "Treere: ", 3*sum(self.rounds[2][i] == 3 for i in range(5))

		points += 4*sum(self.rounds[3][i] == 4 for i in range(5))
		if verbose:
			print "Firere: ", 4*sum(self.rounds[3][i] == 4 for i in range(5))

		points += 5*sum(self.rounds[4][i] == 5 for i in range(5))
		if verbose:
			print "Femmere: ", 5*sum(self.rounds[4][i] == 5 for i in range(5))

		points += 6*sum(self.rounds[5][i] == 6 for i in range(5))
		if verbose:
			print "Seksere: ", 6*sum(self.rounds[5][i] == 6 for i in range(5))

		if verbose:
			print "====================="
			if points >= 42:
				print "Bonus: 50"
			else:
				print "Bonus: 0"
			print "====================="

		if points >= 42:
			points += 50

		#Ett par
		pair_number = 0
		for i in range(5):
			for j in range(5):
				if i != j and self.rounds[6][i] == self.rounds[6][j] and self.rounds[6][i] > pair_number:
					pair_number = self.rounds[6][i]

		points += pair_number * 2
		if verbose:
			print "Ett par: ", pair_number * 2

		#To par
		first_pair = 0
		second_pair = 0
		for i in range(5):
			for j in range(5):
				if i != j and self.rounds[7][i] == self.rounds[7][j] and self.rounds[7][i] > first_pair:
					first_pair = self.rounds[7][i]
				elif i != j and self.rounds[7][i] == self.rounds[7][j] and self.rounds[7][i] > second_pair and self.rounds[7][i] != first_pair:
					second_pair = self.rounds[7][i]

		if first_pair != 0 and second_pair != 0:
			points += (first_pair * 2) + (second_pair * 2)
			if verbose:
				print "To par: ", (first_pair * 2) + (second_pair * 2)
		else:
			print "To par: 0"


		#Tre like
		tre_like = False
		for i in range(5):
			for j in range(5):
				for k in range(5):
					if self.rounds[8][i] == self.rounds[8][j] and self.rounds[8][j] == self.rounds[8][k]:
						if i != j and j != k and k != i:
							points += self.rounds[8][i] * 3
							tre_like = True
							if verbose:
								print "Tre like: ", self.rounds[8][i] * 3
							break
				if tre_like:
					break
			if tre_like:
				break

		if verbose and not tre_like:
			print "Tre like: 0"


		#Fire like
		fire_like = False
		for i in range(5):
			for j in range(5):
				for k in range(5):
					for l in range(5):
						if i != j and j != k and k != l and i != k and i != l and j != l:
							if self.rounds[9][i] == self.rounds[9][j] and self.rounds[9][j] == self.rounds[9][k] and self.rounds[9][k] == self.rounds[9][l]:
								points += self.rounds[9][i] * 4
								fire_like = True
								if verbose:
									print "Fire like: ", self.rounds[9][i] * 4
								break
					if fire_like:
						break
				if fire_like:
					break
			if fire_like:
				break

		if verbose and not fire_like:
			print "Fire like: 0"


		#Liten
		liten = [1, 2, 3, 4, 5]
		if sorted(liten) == sorted(self.rounds[10]):
			points += 15
			if verbose:
				print "Liten: 15"
		else:
			if verbose:
				print "Liten: 0"


		#Stor
		stor = [2, 3, 4, 5, 6]
		if sorted(stor) == sorted(self.rounds[11]):
			points += 20
			if verbose:
				print "Stor: 20"
		else:
			if verbose:
				print "Stor: 0"


		#Hus
		hus_points = 0
		tre_hus = 0
		to_hus = 0
		for i in range(5):
			for j in range(5):
				for k in range(5):
					if self.rounds[12][i] == self.rounds[12][j] and self.rounds[12][j] == self.rounds[12][k]:
						if i != j and j != k and k != i:
							tre_hus = self.rounds[12][i]

		if tre_hus != 0:
			for i in range(5):
				for j in range(5):
					if self.rounds[12][i] == self.rounds[12][j] and i != j and self.rounds[12][i] != tre_hus:
						points += (tre_hus * 3) + (self.rounds[12][i] * 2)
						hus_points = (tre_hus * 3) + (self.rounds[12][i] * 2)
		if verbose:
			print "Hus: ", hus_points



		#Sjanse
		points += sum(self.rounds[13])
		if verbose:
			print "Sjanse: ", sum(self.rounds[13])


		#Yatzy
		if all(x == self.rounds[14][0] for x in self.rounds[14]):
			if verbose:
				print "Yatzy: ", 50
			points += 50
		else:
			if verbose:
				print "Yatzy: ", 0

		return points



if __name__ == "__main__":
	game = Game()

	for i in xrange(0, 45):
		game.throw_dice([])
		game.check_number()


	print game.get_points_at_finish(True)
