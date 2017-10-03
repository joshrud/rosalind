#Genbank Intro
#Josh Rudolph
#9/27/17


from Bio import Entrez

with open("rosalind_gbk.txt", 'r' ) as f:
	genus = f.readline().rstrip('\n')
	date_from = f.readline().rstrip('\n')
	date_to = f.readline().rstrip('\n')

Entrez.email = 'joe@gmail.com'
handle = Entrez.esearch(db="nucleotide", term=genus+"[Organism]", datetype="pdat", mindate=date_from, maxdate=date_to)
record = Entrez.read(handle)

print(record['Count'])
