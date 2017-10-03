#Intro to Binf Armory
#Josh Rudolph
#9/26/17

from Bio.Seq import Seq

with open("rosalind_ini.txt", 'r') as f:
	sequence = Seq(f.readline().rstrip('\n'))

print sequence.count('A'), sequence.count('C'), sequence.count('G'), sequence.count('T')