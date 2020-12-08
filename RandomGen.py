import random

class nom():
	def __init__(self):
		self.complet = list()
		self.final = ""
		self.load()
		self.reduce()

	def load(self):
		self.complet.append(lire_fichier("succube/1.txt"))
		self.complet.append(lire_fichier("succube/2.txt"))
		
	def reduce(self):
		for i in range(len(self.complet)):
			count = random.randint(0, len(self.complet[i])-1)
			self.final += self.complet[i][count]

def lire_fichier(f):
	with open(f, "r") as file:
		l=file.read()
	return l.splitlines()


def main():
	n=nom()
	print(n.final)
	
main()