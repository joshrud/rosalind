#rabbit fibonacci
#Josh Rudolph
#9/22/17

def rabbitFib(n,k):
	pairs = [1,1]
	for i in range(n):
		if i == 0 or i == 1:
			continue
		pairs.append(pairs[i-2]*k + pairs[i-1])
	return str(pairs[-1])

def main():
	n = 34
	k = 3
	print(rabbitFib(n, k))








if __name__=="__main__":
	main()
 