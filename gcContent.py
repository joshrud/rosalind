#fasta gc-content
#Josh Rudolph
#9/26/17

def main():
	sequences = []
	title = ""
	seq = []
	GCcontents = []
	with open("rosalind_gc.txt") as f:
		i = 0
		for line in f:
			if '>' in line:
				if i != 0:
					sequences.append((title, "".join(seq)))
					title = ""
					seq = []
				title = line.rstrip('\n').lstrip('>')
			else:
				seq.append(line.rstrip('\n'))
			i+=1
		sequences.append((title, "".join(seq)))


	for n in sequences:
		GCcontents.append((n[0], getGCcontent(n[1])))

	print("GCcontents: " , GCcontents)
	bestGC = max(GCcontents, key=lambda x:x[1])
	print(bestGC[0])
	print(bestGC[1])


			

def getGCcontent(seq):

	GCs = 0
	for i in range(len(seq)):
		if seq[i] == 'G' or seq[i] == 'C':
			GCs +=1

	return 100*float(GCs)/float(len(seq))



if __name__=="__main__":
	main()
 
