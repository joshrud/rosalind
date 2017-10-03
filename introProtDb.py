#Intro to Protein Databases
#Josh Rudolph
#9/27/17


from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw("Q6FN12")
record = SwissProt.read(handle)

refs = record.cross_references
processes = []
for i in refs:
	if i[0] == 'GO':
		processes.append(i[2])

prot_procs = []
for j in processes:
	if j[0]=='P':
		prot_procs.append(j[2:])

print("\n".join(prot_procs))