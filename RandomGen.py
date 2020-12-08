import random

class nom():
	def __init__(self, type):
		self.complet = list()
		self.final = ""
		self.load(type)
		self.reduce()

	def load(self, type):
		self.complet.append(lire_fichier(type + "/1.txt"))
		self.complet.append(lire_fichier(type + "/2.txt"))
		
	def reduce(self):
		for i in range(len(self.complet)):
			count = random.randint(0, len(self.complet[i])-1)
			self.final += self.complet[i][count]

def lire_fichier(f):
	with open(f, "r") as file:
		l=file.read()
	return l.splitlines()

def choisir_type(type):
	if type==1:
		return "succube"
	else:
		return "marcheur"

def main(t, n):
	type = choisir_type(t)
	for i in range(0, n):
		n = nom(type)
		print(n.final)
	print("\n")
	
main(1, 10)
main(2, 10)