#hamming distance
#Josh Rudolph
#9/26/17

if __name__ == "__main__":

	with open("rosalind_hamm.txt", 'r') as f:
		string1 = f.readline().rstrip('\n')
		string2 = f.readline().rstrip('\n')

	distance = 0
	for i in range(len(string1)):
		if string1[i] != string2[i]:
			distance +=1

	print(distance)

