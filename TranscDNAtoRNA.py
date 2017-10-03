#transcribing dna to rna
#Josh Rudolph
#9/22/17


RNA = []
string = "TCGGGTCCCGGGAAGCGCACCAACAACTACCTGACCCTACAGATTTGCTGTAAACGCATGGATTGAGCGTAACGCTGAGCTTTTCTACCCAGCGAGCAGGTCAGGGCAGCTTGTCAGGCTCGTAAAGGACACGCTCTTGGTACTTTACGTCCTCATAGGATCGCTGTTGTGTCCACATATGCTTCCCTATTTAGTATCGCTCCCGCCCTTCAGGACGCCGGATACATTTCCAGGGCAGATCCGACAGTTACACATGGTTCAGTTGGACTCGCTGTCTCCCGTTGGGTCTATTCTCGCGTCTTATTTGTTAAGCGGAGTACTGCTTTGATGGATGACCGACGAAACAAGCCAACAGGTCTGATATAGCATGTTTTGGAACCGTGTAAATAAAATTAGGCGCATCAGCATGTGAAGAAAGCTACCATCTCTAAGTGATCCATATTTGCCTGGAAATACGCCGACCGTTGTTCGCGACTGACAGGTAACCGGGACAGATGCATGTTTCCCGCCGTTTGATGACGGCCAGAATTCGCCACAATCTTTTTAGGTTTGCTTATTCCAAATCGGAAATGAGAGTTAACCGTATAGGAACGTCGTCGCTACCCTATCACAGGAACTGGCCGGATTGCGTCGTCCCCCGCGCTTTGCCGGGATTATGTTAGGATCGCGTAGGATCAACGCAGGTTTTATCTTCAGCATTGAGACGGGGTGTTCTGGGAATTGCCATGGATGGAGTGTAGTAGATAGCGGGGGAGCCTCACCCGACGAGTACAGCTTTGTAGGCATGCTTAACCGTAATTGAATAGATCTTTTGATCGTCTCACCACCCCCTACATCTCACCCCATCGGACACCCAATGGGTGCGCTTATCAGGGAACGCGCACCGAGGAGCAAAAAAACGACGTCCAAACGCCTCGCTACGAGATGTCATCCATGCCTGTCCTTGCGTCGTTCGATCGG"
for n in string:
	if n=='T':
		RNA.append('U')
	else:
		RNA.append(n)

print("".join(RNA))