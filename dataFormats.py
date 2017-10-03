#Data Formats
#Josh Rudolph
#9/27/17


from Bio import Entrez, SeqIO


with open("rosalind_frmt.txt", 'r' ) as f:
	entries = f.readline().rstrip('\n').split(' ')

Entrez.email = 'hi@example.com'
handle = Entrez.efetch(db="nucleotide", id=entries, rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print min(records, key=lambda x: len(x.seq)).format("fasta")


